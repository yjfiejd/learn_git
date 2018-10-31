import ctypes
import os
import platform
# from memory_profiler import profile
from collections import defaultdict
import timeit
import copy
import json

file_path = os.path.dirname(__file__)

extension = 'dylib'
if not platform.platform().find('Linux'):
    extension = 'so'

lib = os.path.join(file_path, 'libmap_concept.' + extension)
map_concept = ctypes.PyDLL(lib)


class IntArray(ctypes.Structure):
    _fields_ = [
        ("statuscode", ctypes.c_int),
        ("sid", ctypes.POINTER(ctypes.c_int)),
        ("size", ctypes.c_int),
        ("errormessage", ctypes.c_char_p)
    ]


class CharArray(ctypes.Structure):
    _fields_ = [
        ("statuscode", ctypes.c_int),
        ("sid", ctypes.POINTER(ctypes.c_int)),
        ("chararray", ctypes.POINTER(ctypes.c_char_p)),
        ("size", ctypes.c_int),
        ("errormessage", ctypes.c_char_p)
    ]


map_concept.get_concept.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
map_concept.get_concept.restype = ctypes.POINTER(IntArray)

map_concept.get_parent.argtypes = [ctypes.c_int, ctypes.c_char_p]
map_concept.get_parent.restype = ctypes.POINTER(IntArray)

map_concept.get_redundancy.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
map_concept.get_redundancy.restype = ctypes.POINTER(CharArray)

map_concept.get_max_match.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
map_concept.get_max_match.restype = ctypes.POINTER(CharArray)

map_concept.get_id_attr.argtypes = [ctypes.c_int, ctypes.c_char_p]
map_concept.get_id_attr.restype = ctypes.POINTER(ctypes.c_char)

map_concept.get_unit_code.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
map_concept.get_unit_code.restype = ctypes.POINTER(ctypes.c_char)

map_concept.get_domain.argtypes = None
map_concept.get_domain.restype = ctypes.POINTER(ctypes.c_char_p)

model_path = os.path.join(file_path, '../data/EncryptData/').encode('utf-8')


def multi_concept(text, mode=1):
    if mode == 0:
        candidates, record = generate_candidates(list(text))
    elif mode == 1:
        candidates, record = generate_candidates(get_max_match('disease', text))
    return score_it(candidates, record)


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.paths = []
        self.maxreach = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def travel_all_paths_util(self, u, d, visited, path):
        visited[u] = True
        path.append(u)

        if u == d:
            temp = copy.deepcopy(path)
            self.paths.append(temp)
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.travel_all_paths_util(i, d, visited, path)
        path.pop()
        visited[u] = False

    def travel_all_paths(self, s, d):
        visited = [False] * (self.V)
        path = []
        self.travel_all_paths_util(s, d, visited, path)


def generate_string(symbol_list, index_list):
    start = 0
    result = []
    for index in index_list[1:]:
        result.append(''.join(symbol_list[start:index]))
        start = index
    return result


def generate_candidates(symbol_list):
    record = {}
    matrix_lens = len(symbol_list)
    mark_table = [['O'] * matrix_lens for _ in symbol_list]
    graph = Graph(matrix_lens + 1)

    for y_index in range(matrix_lens):
        pre_result = set()
        for length in range(matrix_lens - y_index):
            search_str = ''.join(symbol_list[y_index:y_index + length + 1])
            if search_str not in record:
                record[search_str] = set(get_concept_id('disease', search_str))
            temp_result = record[search_str]
            if not temp_result:
                mark_table[y_index][y_index + length] = 'P'
            elif temp_result.issuperset(pre_result) and not pre_result:
                mark_table[y_index][y_index + length] = 'S'
                pre_result.update(temp_result)
            elif temp_result.issuperset(pre_result) and temp_result.issubset(pre_result):
                mark_table[y_index][y_index + length] = 'Y'
            elif temp_result.issuperset(pre_result):
                mark_table[y_index][y_index + length] = 'X'
                break
            else:
                mark_table[y_index][y_index + length] = 'Y'

    for i, line in enumerate(mark_table):
        for j, x in enumerate(line):
            if x in ["S", "Y"]:
                graph.add_edge(i, j + 1)
                graph.maxreach = max(graph.maxreach, i + 1)

    graph.travel_all_paths(0, matrix_lens)
    if not graph.paths:
        graph.travel_all_paths(0, graph.maxreach)
    all_path = graph.paths
    candidates = []
    for path in all_path:
        candidate = generate_string(symbol_list, path)
        candidates.append(candidate)
    return candidates, record


def score_it(candidates, record):
    result_dict = defaultdict(set)
    redundancy_record = {}
    for i, candidate in enumerate(candidates):
        for item in candidate:
            if not item in record:
                record[item] = get_concept_id(b'disease', item)
            result_dict[i].update(record[item])

    def cal_missing_part(candidate):
        left = set()
        for item in candidate:
            if not item in redundancy_record:
                redundancy_record[item] = get_redundancy('disease', item)
            for match in redundancy_record[item]:
                left.update(match[1])
        return len(''.join(left))

    missing_parts = [cal_missing_part(candidate) for candidate in candidates]
    reserved_candidates = [i for i, score in enumerate(missing_parts) if score == min(missing_parts)]

    def remove_subset(reserved_candidates):
        result = copy.deepcopy(reserved_candidates)
        for i in reserved_candidates:
            for j in reserved_candidates:
                if result_dict[i] < result_dict[j]:
                    try:
                        result.remove(i)
                    except:
                        pass
        return result

    reserved_candidates = remove_subset(reserved_candidates)
    concept_lengths = [len(candidate) for candidate in candidates]
    if concept_lengths:
        min_concept_lengths = min([length for i, length in enumerate(concept_lengths) if i in reserved_candidates])
        reserved_candidates = [i for i, score in enumerate(concept_lengths) if
                               score == min_concept_lengths and i in reserved_candidates]
    else:
        reserved_candidates = []

    def cal_using_rate(reserve_cadicates):
        rate_list = []
        for item in reserve_cadicates:
            i = 0
            for cha in candidates[item]:
                i += len(set(cha))
            rate_list.append(i)
        return [reserve_cadicates[i] for i, score in enumerate(rate_list) if score == max(rate_list)]

    result = cal_using_rate(reserved_candidates)
    return [list(result_dict[i]) for i in result]


def test_speed(text, num=5):
    print(timeit.timeit('multi_concept(text, mode=1)', number=num,
                        setup="from __main__ import multi_concept; text = '{}' ".format(text)) / num)


def strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
            inside_code -= 65248

        rstring += chr(inside_code)
    return rstring


def get_disease_concept_id(text, maxlen=50):
    r1 = get_concept_id('disease', text)
    if len(r1) == 1 or len(r1) == 0 or len(text) > maxlen:
        return r1
    else:
        r2 = multi_concept(text, 1)
        if r2:
            return r2[0]
        else:
            return []


def get_concept_id(domain, text):
    text = strQ2B(text).lower().strip()
    ptr = map_concept.get_concept(text.encode('utf-8'), domain.encode('utf8'), model_path, 0)
    statuscode = ptr[0].statuscode
    if statuscode != 0:
        message = ptr[0].errormessage.decode('utf8')
        raise Exception(message)
    sid = ptr[0].sid
    size = ptr[0].size
    result = []
    for x in range(size):
        result.append(sid[x])
    if not result:
        ptr = map_concept.get_concept(text.encode('utf-8'), domain.encode('utf8'), model_path, 1)
        statuscode = ptr[0].statuscode
        if statuscode != 0:
            message = ptr[0].errormessage.decode('utf8')
            raise Exception(message)
        sid = ptr[0].sid
        size = ptr[0].size
        for x in range(size):
            result.append(sid[x])
    map_concept.free_IntArray(ptr)
    return result


def get_redundancy(domain, text):
    result = []
    text = strQ2B(text).lower()
    ptr = map_concept.get_redundancy(text.encode('utf-8'), domain.encode('utf8'), model_path)
    for x in range(ptr[0].size):
        result.append((ptr[0].sid[x], ptr[0].chararray[x].decode('utf8').strip().split()))
    map_concept.free_CharArray(ptr)
    return result


def get_max_match(domain, text):
    result = []
    text = strQ2B(text).lower()
    ptr = map_concept.get_max_match(text.encode('utf-8'), domain.encode('utf8'), model_path)
    for x in range(ptr[0].size):
        result.append(ptr[0].chararray[x].decode('utf8').strip())
    map_concept.free_CharArray(ptr)
    return result


def get_ancestor(sid):
    ptr = map_concept.get_parent(sid, model_path)
    ancestor = ptr[0].sid
    size = ptr[0].size
    result = []
    for x in range(size):
        result.append(ancestor[x])
    map_concept.free_IntArray(ptr)
    return [sid] + result


def get_id_attr(id, attr):
    ptr = map_concept.get_id_attr(int(id), attr.lower().strip().encode('utf-8'), model_path)
    result = ctypes.cast(ptr, ctypes.c_char_p).value.decode('utf-8')
    map_concept.free_Char(ptr)
    if attr == 'parent':
        result = json.loads(result)
    # 返回一个单位，检验不跑nlp
    if attr == 'unit':
        result = json.loads(result)
        if result:
            result = result[0]
    return result


def get_unit_code(unit):
    ptr = map_concept.get_unit_code(unit.lower().strip().encode('utf-8'), model_path)
    result = ctypes.cast(ptr, ctypes.c_char_p).value.decode('utf-8')
    map_concept.free_Char(ptr)
    return result


def get_domain():
    ptr = map_concept.get_domain()
    result = []
    i = 0
    while ptr[i]:
        result.append(ptr[i].decode('utf8'))
        i += 1
    return result


# @profile
def test():
    for i in range(100000):
        get_disease_concept_id("高血压")


domain = get_domain()
if __name__ == "__main__":
    print(domain)
    print(get_redundancy("lab", "实验室检查"))
    print(get_concept_id("symptom", "咳嗽ewf"))
    print(get_disease_concept_id("射精延迟"))
    print(get_disease_concept_id("脓毒症"))
    print(get_disease_concept_id("败血症"))
    print(get_disease_concept_id("眼白化病"))
    print(get_disease_concept_id("vsd"))
    print(get_concept_id("eeg", "顶区异常波"))
    print(get_redundancy("disease", "消化道出血"))
    print(get_redundancy("labsub", "网织红细胞hb含量测定"))
    print(get_redundancy("ucg", "左室收缩末期容量"))
    print(get_ancestor(111))
    print(get_max_match("disease", "消化道出血高血压糖尿病症状"))
    print(get_disease_concept_id("胸腹疼痛主动脉夹层高血压病COPD脑梗后右股骨颈骨折术后"))
    print(get_concept_id('disease', '感知觉缺失'))
    print(get_concept_id('disease', '尿路感染 系统性红斑狼疮'))
    print(get_disease_concept_id('尿路感染 系统性红斑狼疮'))
    print(get_id_attr(146258, "standard_ch"))
    print(get_unit_code("克"))
    print(multi_concept('充血性脾大', 1))
    print(get_max_match('disease', 'sdfdsf高血压/vsd'))
    print(get_concept_id('hpg', '羊水清'))
    print(get_id_attr(151434, "standard_ch"))
    print(get_concept_id('pe', '体温37.0℃'))
    print(get_max_match('pe', '体温37.0℃'))
    print(get_id_attr(147798, "standard_ch"))
    print(get_redundancy('pe', '体温37.0℃'))
    print(get_id_attr(147798, "unit"))
    print(get_id_attr(146258, "units"))
    print(get_id_attr(147726, "parent"))
    print(get_id_attr(151425, "domain"))
    print(get_unit_code('℃'))
    print(get_concept_id('person', '爷爷'))
    print(get_concept_id('substance', '猪肉'))
    print(get_concept_id('modifier', '多发'))
    print(get_concept_id('substance', '猪肉'))
    print(get_concept_id('body', '右肺门'))
    print(get_concept_id('morphology', '溃疡性炎症'))
