"""
输入：一个json文件的地址（含10个json）

输出：返回每一个json_checklist (共计10个) list，   方便后续查找 id - text - category
[{'id': 106,
  'pos': [1, 18],
  'relations': [],
  'timestamps': 106,
  'category': 28,
  'text': 'ClinicalDiagnosis'},
  ...]

"""

import json
import sys
import re
import os
from collections import defaultdict

# 子函数
def remove_unlabel(annotation):
    data = sorted(annotation['labels'], key=lambda x: x['pos'][0])
    flag = 0
    unlabel = []
    for item in data:
        # if re.search('鉴别诊断',annotation['content'][item['pos'][0]:item['pos'][1] + 1]):
        #     print('*******',annotation['id'])

        if re.match(r'^鉴别诊断$', annotation['content'][item['pos'][0]:item['pos'][1] + 1]) or item['category'] == 44:
            # print('---------------', annotation['id'])
            # print(annotation['content'][item['pos'][0]:item['pos'][1] + 1])

            flag = 1
            unlabel.append(item['id'])
        elif flag == 1:
            # print(annotation['content'][item['pos'][0]:item['pos'][1] + 1], annotation['id'])
            if item['category'] == 28 or item['category'] == 44:
                flag = 0
            unlabel.append(item['id'])
        elif re.match(r'^\s+$', annotation['content'][item['pos'][0]:item['pos'][1] + 1]):
            unlabel.append(item['id'])

    rel = [i for i in annotation['relations'] if (i['src'] not in unlabel and i['dst'] not in unlabel)]
    lab = [i for i in annotation['labels'] if i['id'] not in unlabel]
    annotation['labels'] = lab
    annotation['relations'] = rel

    return annotation

# 子函数
def train2anno(train):
    result = {'concepts': []}
    train = remove_unlabel(train)
    sorted_label = sorted(train['labels'], key=lambda x: x['pos'][0])
    temp = {'id': 0, 'pos': [0, 0], 'relation': [], 'timestamps': 0}
    for j, item in enumerate(sorted_label):
        result['concepts'].append(
            {'id': item['id'], 'pos': [item['pos'][0], item['pos'][1] + 1], 'relations': [], 'timestamps': item['id'],
             'category':item['category'],'text':train['content'][item['pos'][0]:item['pos'][1] + 1]})

    for j, item in enumerate(train['relations']):
        src = item['src']
        dst = item['dst']
        for ii in result['concepts']:
            if ii['timestamps'] == dst:
                for jj in result['concepts']:
                    if jj['timestamps'] == src:
                        ii['relations'].append({"text": jj['text'], "src_id": jj['id'], 'type': item['category']})

    anno = {'NLPResult': result, 'rawText': train['content']}

    return anno

# 子函数open_json
def open_json(files):
    if files.endswith('.json'):
        with open(files, 'r', encoding='utf8') as f:
            return json.load(f)

    else:
        result = []
        PATH = os.listdir(files)
        for file in PATH:
            with open(files + file, 'r', encoding='utf8') as f:
                result.extend(json.load(f))
        return result



# 子函数：正则，获取字符中的两个数字， a, b
def find_a_b_in_json_path(json_path):
    pattern = r'.*annotation(\d{5})-(\d{5})'
    match_a_b = re.match(pattern, json_path, re.I)
    a = int(match_a_b.group(1))
    b = int(match_a_b.group(2))
    return a, b



#  主函数
def find_all_checklist_json(json_path):
    """
    输入：一个json地址, 包括10个json的地址
    json_path = "../python_test_data/json_file/annotation37529-37538.json"


    输出：查询节点信息的list，每个json对应不同的查找字典
    [{'id': 106, 'pos': [1, 18], 'relations': [], 'timestamps': 106, 'category': 28, 'text': 'ClinicalDiagnosis'}, ...]
    """

    # 未来这句需要用一个函数代替
    a, b = find_a_b_in_json_path(json_path)

    anno_id_list = [i for i in range(a, b+1)] # 举例：range范围（37538+1）-37529

    all_checklist_json_list = []  # 收集10个 checklist_json
    for anno_id in anno_id_list:
        data = open_json(json_path)
        a = set()
        for item in data:
            if item["id"] == anno_id:
                each_check_dict = train2anno(item)['NLPResult']['concepts']
        all_checklist_json_list.append(each_check_dict)
    return all_checklist_json_list




# 测试
# json_path = "../python_test_data/json_file/annotation37529-37538.json"

# json_path = "../python_test_data/json_file/annotation39469-39530.json"
#
# all_checklist_json_list = find_all_checklist_json(json_path)
# print('all_checklist_json_list = ', all_checklist_json_list)
# print('len(all_checklist_json_list) = ', len(all_checklist_json_list))



