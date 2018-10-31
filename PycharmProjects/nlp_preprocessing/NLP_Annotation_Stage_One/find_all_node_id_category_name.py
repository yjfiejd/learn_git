"""
输入：
1) json_path -> 为了这个json文件中的label  -> 为了获得： ‘id’ ：‘tag’ （category）
2) export_path     -> 为了获得： ‘tag’（category）： ‘name’
3) json_path -> 获得的loop_node_more_than_2 : [[[41], [44], [56]], [[121, 15], [26], [58]], ...]  -> 父节点大于2的环上的节点（每段中，每个环中）

输出：
1）{‘id’:{'tag':'name'}} -> 找到是哪些点（目前定义为环中父节点大于2的）造成了环 -> 它的含义是

[{41: {7: '身体结构'}, 44: {7: '身体结构'}, 56: {7: '身体结构'}},
 {121: {53: '名词性异常表现'}, 15: {7: '身体结构'}, 26: {7: '身体结构'}, 58: {7: '身体结构'}},...]

"""
import json

from NLP_Annotation_Stage_One.find_all_loop_node_more_than_2 import *

# 1) 获取 export文件中的category
def get_export_file_category(export_file_path):
    with open(export_file_path, "r") as f:
        export_file = json.load(f)
    export_file_category = export_file['categories']
    return export_file_category


# 2) 获取json文件中的label部分
def get_json_file_label(json_path):
    with open(json_path, "r") as f:
        one_json = json.load(f)
    one_json_labels = []
    for i in one_json:
        one_json_labels.append(i['labels'])
    return one_json_labels


# 3） 获得loop_node_more_than_2
# set_loop_nodes_more_than_2_list = find_loop_node_more_than_2(json_path)


# 4) 获得 一段话中环的， 'id' - 'category'
def find_node_to_category_list(loop_node_more_than_2, one_json_labels):
    """
    :param loop_node_more_than_2: json中，十段话中所有的环中，每段话父节点大于2的节点 [[[41], [44], [56]], [[121, 15], [26], [58]],...]
    :param one_json_labels: json文件中，十段话中每段的label部分集合  [[{'id': 106, 'pos': [1, 17], 'category': 28},...]
    :return: [[{41: 7}, {44: 7}, {56: 7}], [{121: 53}, {15: 7}, {26: 7}, {58: 7}],...]
    """

    # 先把每一段中的，某个环中父节点大于2的节点list，拆开[[121, 15], [26], [58]], -> [121, 15, 26, 58]
    new_loop_more_than_2 = []
    for i in loop_node_more_than_2:
        list_1 = []
        for j in i:
            for k in j:
                list_1.append(k)
        new_loop_more_than_2.append(list_1)  # 举例 [121, 15, 26, 58]

    all_node_id_category_list = []
    for k in range(len(new_loop_more_than_2)):  # 循环10段话
        loop_node_more_than_2_k = new_loop_more_than_2[k]  # 取出第一段话中的，环节点数大于2的节点
        one_json_labels_k = one_json_labels[k]  # 取出第一段话中的label，开始匹配

        node_id_category_list = []
        for i in loop_node_more_than_2_k:  # 取出第一段话中的，第一个环中的父节点个数大于2的节点：举例: [121, 15, 26, 58] 中的i = 121

            node_id_category_dict = dict()  # 准备dict
            for j in one_json_labels_k:  # 在第一段label中寻找对应的category值
                if i == j['id']:
                    node_id_category_dict[i] = j['category']  # 构造字典
            node_id_category_list.append(node_id_category_dict)  # append list

        all_node_id_category_list.append(node_id_category_list)  # append all list
    return all_node_id_category_list


# 5) 获得一段话中的， 二维字典：‘id’ -> 'category' -> 'name'
def find_paragraph_node_category_name(test_a, export_file_category):
    """
    输入：每段话中, test_a，环中父节点大于2的节点id : 它的tag(category)

    输出：node_id_category_name_dict  每段话中，环中父节点大于2的节点 {id: {category: name}, ...}
    """
    # 第一段话结果1: 获得 [[{53: '名词性异常表现'}], [{7: '身体结构'}], [{60: '影像'}], [{7: '身体结构'}]]
    list_b = []
    for i in test_a:  # 获得每一段中，每个环节点字典 {41: 7}
        # list_bb = []
        for k in i:  # 获得字典中的value值：7 ，i[k]
            list_bb = []
            list_cc = []
            dict_2 = dict()
            new_dict_1 = dict()
            for j in export_file_category:  # 去export中搜索
                if i[k] == j['id']:
                    dict_2[i[k]] = j['name']
            #                 print(dict_2)
            list_bb.append(dict_2.copy())  # 第一段中的第一个环dict，匹配完毕
        list_b.append(list_bb)  # 第一段中的其他环，dict 匹配完毕


    # 第一段话结果2： 把所有的key拿出来，与list_b组成新的二维字典
    key_list = []  # 为了获得 [119, 27, 159, 58]
    for i in test_a:  # 输入 test_a = [{41: 7}, {44: 7}, {56: 7}]
        for j in i:
            key_list.append(j)

    # 第一段话组合结果：结果1与结果2获得二维字典： {119: {53: '名词性异常表现'}, 27: {7: '身体结构'}, 159: {60: '影像'}, 58: {7: '身体结构'}}
    node_id_category_name_dict = dict()
    for i in range(len(key_list)):
        node_id_category_name_dict[key_list[i]] = list_b[i][0]

    return node_id_category_name_dict


# 6) 获得十段话中的 二维字典：‘id’ -> 'category' -> 'name'
def get_all_node_id_category_name(all_node_id_category_list, export_file_category):
    """
    输入：1个json中的，'id' 与 'tag' 字典列表
    all_node_id_category_list： [[{41: 7}, {44: 7}, {56: 7}],[{121: 53}, {26: 7}, {58: 7}],....]

    输出：1个json中的，'id' 与 ‘tag’:'name'二维字典列表
    [{41: {7: '身体结构'}, 44: {7: '身体结构'}, 56: {7: '身体结构'}},..]
    """
    all_node_id_category_name_list = []
    for i in all_node_id_category_list:
        node_id_category_name_list = find_paragraph_node_category_name(i, export_file_category)
        all_node_id_category_name_list.append(node_id_category_name_list)
    return all_node_id_category_name_list


# 实验
#
# # 1) 输入2个文件的地址
# json_path = "/Users/synyi/Desktop/annotation37529-37538.json"
# export_file_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/NLP_Annotation_Stage_One/export.json"
#
# # 2） 获得one_json_file_label + export_file_category
# one_json_file_label = get_json_file_label(json_path)
# export_file_category = get_export_file_category(export_file_path)
#
# # 3) 获得 ‘id’-> 'tag'  字典列表 [[{41: 7}, {44: 7}, {56: 7}],...]
# all_node_id_category_list = find_node_to_category_list(set_loop_nodes_more_than_2_list, one_json_file_label)
#
# print(all_node_id_category_list)
#
# # 4) 获得最后结果：{41: {7: '身体结构'}, 44: {7: '身体结构'}, 56: {7: '身体结构'}},...}
# all_node_id_category_name = get_all_node_id_category_name(all_node_id_category_list, export_file_category)
# print('\n')
# print(all_node_id_category_name)


# 7 ) 包装为一个函数：

def find_all_node_id_category_name(json_path, export_file_path):  # 1)
    one_json_file_label = get_json_file_label(json_path)  # 2)
    export_file_category = get_export_file_category(export_file_path)  # 2)

    set_loop_nodes_more_than_2_list = find_loop_node_more_than_2(json_path) # 2.5）

    all_node_id_category_list = find_node_to_category_list(set_loop_nodes_more_than_2_list, one_json_file_label)  # 3)

    all_node_id_category_name = get_all_node_id_category_name(all_node_id_category_list, export_file_category)  # 4)

    return all_node_id_category_name


# 测试：
# json_path = "../python_test_data/json_file/annotation37529-37538.json"
# json_path = "../python_test_data/json_file/annotation38125-38225.json" # 100个json文件


# json_path = "../python_test_data/json_file/annotation39469-39530.json"
# export_file_path = "../python_test_data/export.json"
# all_node_id_category_name = find_all_node_id_category_name(json_path, export_file_path)
# print('all_node_id_category_name: ' , all_node_id_category_name)
