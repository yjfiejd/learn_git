"""
输入：
1）json 文件路径
2) relation.json 文件路径

输出：




"""

import json

from NLP_Annotation_Stage_One.find_all_loop_node_more_than_2 import *

# 1） 获得relation.json文件路径
def get_relation_file_name(relation_path):
    with open(relation_path, "r") as f:
        export_file = json.load(f)
    return export_file


# 2）获得 json中的relation中内容
def get_json_file_relations(json_path):
    with open(json_path, "r") as f:
        one_json = json.load(f)
    one_json_relations = []
    for i in one_json:
        one_json_relations.append(i['relations'])
    return one_json_relations


# 3）获得一个json文件中，带环中父节点大于2的节点  — —> 所对应的relations
# loop_node_more_than_2 = find_loop_node_more_than_2(json_path)


# 3.5）获得环中父节点大于2的节点的，新的list形式， 拆开了一些[[121, 15], 26, 58]
def get_new_loop_more_than_2(loop_node_more_than_2):
    new_loop_more_than_2 = []
    for i in loop_node_more_than_2:
        list_1 = []
        for j in i:
            for k in j:
                list_1.append(k)
        new_loop_more_than_2.append(list_1)  # 举例 [121, 15, 26, 58],
    return new_loop_more_than_2


# 4.1）
# 找到 第一段话中 父节点>2的节点与父节点边的集合
def find_loop_node_and_parent_para(aa, bb):
    """
    输入：每段话中
    1）父节点>2的节点：  aa = [41, 44, 56]
    2）注意，bb需要提前处理，合并为1个list，不是3个list，
    环中所有的节点&父节点集合：bb = [[{139: [138], 41: [139, 140], 138: [], 140: [138]}],
   [{45: [47], 44: [45, 46], 47: [], 46: [47]}],
   [{57: [59], 56: [57, 58], 59: [], 58: [59]}]]

    输出：每段话中
    父节点>2的节点 & 父节点 边的集合
    [(41, 139), (41, 140), (44, 45), (44, 46), (56, 57), (56, 58)]

    """
    # 0）提前处理bb集合，多个环，合并在一起，然后查找。
    new_bb = []
    for i in bb:
        new_bb.extend(i)
    # print(new_bb)

    # 1） 把父节点>2的环中节点，对应的边取出  ——> 获得结果1：[{41: [139, 140]}, {44: [45, 46]}, {56: [57, 58]}]
    list_loop_node_and_parent_para = []
    for i in aa:  # 数字，aa的长度
        list_2 = dict()
        for k in new_bb:  # k 是第一个去除了[] 的 {139: [138], 41: [139, 140], 138: [], 140: [138]}
            for j in k:  # j是keys： 139、41、138、140
                if i == j:
                    list_2[j] = k[j]
        list_loop_node_and_parent_para.append(list_2)

    # 2） 修改格式  --> 获得结果2：[{41: 139}, {41: 140}, {44: 45}, {44: 46}, {56: 57}, {56: 58}]
    list_0 = []
    for node_and_father in list_loop_node_and_parent_para:
        for key in node_and_father:
            #         print(key)
            #         print(node_and_father[key])
            len_of_father = len(node_and_father[key])
            for j in range(len_of_father):
                dict_2 = dict()
                dict_2[key] = node_and_father[key][j]
                list_0.append(dict_2)
    list_node_father = []
    for i in list_0:
        list_node_father.append(list(i.items())[0])

    return list_node_father


# 4.2） 找到 第一段话中 父节点>2的节点与父节点边的集合对应的 category
def get_loop_node_category_para(list_loop_node_and_parent_para, json_file_relations_i):
    """
    # 输入：
    # 1）第一段话中 父节点>2的节点与父节点边的集合
    # list_loop_node_and_parent_para = find_loop_node_and_parent_para(aa, bb)
    # 2）json文件中，第一段话中的relation集合
    # json_file_relations_i = json_file_relations[0]

    # 输出：获得 >2父节点的节点与父节点的关系category
    # [135, 135, 124, 124, 124, 124]
    """
    loop_node_category_para = []
    for item in list_loop_node_and_parent_para:
        loop_node_father = item[0]
        loop_node_son = item[1]

        for j in json_file_relations_i:
            if j['dst'] == loop_node_father and j['src'] == loop_node_son:
                loop_node_category_para.append(j['category'])
    return loop_node_category_para


# 5）找到category 对应的 关系'id'
def find_node_parent_relation_para(relation_file_name, loop_node_category_para):
    """
    输入：
    1） relation_file_name ： 'id' ('category') -> 'name'
    2） loop_node_category_para : 第一段文字中 找到的父子节点关系 'category'
    输出：
    1) 找到 某条边 -> 它的关系  -> [{135: '是_的主体/上级'},{135: '是_的主体/上级'},{124: '是_的某属性'},...]
    """
    node_parent_relation = []
    for i in loop_node_category_para:
        node_parent_relation_dict = dict()
        for j in relation_file_name:
            if j['id'] == i:
                node_parent_relation_dict[i] = j['name']
                node_parent_relation.append(node_parent_relation_dict)
    return node_parent_relation


# test

# 【程序逻辑如下：】

# # 获得relation.json文件路径
# relation_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/NLP_Annotation_Stage_One/relation.json"
# relation_file_name = get_relation_file_name(relation_path)
#
# # 获得 json中的relation中内容
# json_path = "/Users/synyi/Desktop/annotation37529-37538.json"
# json_file_relations = get_json_file_relations(json_path)
#
# # 1) 通过2个path 找到了 aa, bb
# loop_node_more_than_2 = find_loop_node_more_than_2(json_path)
# new_loop_more_than_2 = get_new_loop_more_than_2(loop_node_more_than_2)
#
# all_loop_edges_in_one_json_list = find_all_loop_edges_in_one_json_list(json_path)
# dict_loop_node_parent = find_dict_loop_node_parent(all_loop_edges_in_one_json_list)
#
#
# json_file_relations = get_json_file_relations(json_path)
#
#
# # 把所有的边存下来
# all_loop_nodes_and_parents = []
# all_loop_nodes_and_parents_relation = []
#
# # 把所有的边的关系存下来
#
# for i in range(len(json_file_relations)):
#     print(i)
#     aa = new_loop_more_than_2[i]  # 输入1.1
#     bb = dict_loop_node_parent[i]  # 输入1.2
#
#     # 2) 输出了：[(41, 139), (41, 140), (44, 45), (44, 46), (56, 57), (56, 58)]
#     list_loop_node_and_parent_para = find_loop_node_and_parent_para(aa, bb)  # 输入2.1
#     all_loop_nodes_and_parents.append(list_loop_node_and_parent_para)
#
#
#     # print('环中，父节点大于2的节点，所连接的边共{}条，分别为：\n {},：'.format(len(list_loop_node_and_parent_para), list_loop_node_and_parent_para))
#
#     # 3)
#
#     json_file_relations_i = json_file_relations[i]  # 输入2.2
#
#     # 4) 输出了 [135, 135, 124, 124, 124, 124]
#     loop_node_category_para = get_loop_node_category_para(list_loop_node_and_parent_para,
#                                                           json_file_relations_i)  # 输入3.2
#
#     # 5）输出了：[{135: '是_的主体/上级'}, {135: '是_的主体/上级'}, ...]
#
#     relation_file_name = get_relation_file_name(relation_path)  # 输入3.1
#     node_parent_relation = find_node_parent_relation_para(relation_file_name, loop_node_category_para)
#     all_loop_nodes_and_parents_relation.append(node_parent_relation)
#     # print('环中，父节点大于2的节点，所连接的边relation属性为：\n ', node_parent_relation)


def find_all_node_parent_relations(json_path, relation_path):
    """
    :param json_path:  一个json文件的地址
    :param relation_path: 一个relation文件的地址
    :return:
    输出1）：all_loop_nodes_and_parents -> 环中所有父节点大于2的节点，所连接的边的集合
    输出2）：all_loop_nodes_and_parents_relation -> 环中所有父节点大于2的节点，所连接的边的relation集合
    """
    relation_file_name = get_relation_file_name(relation_path)
    json_file_relations = get_json_file_relations(json_path)


    loop_node_more_than_2 = find_loop_node_more_than_2(json_path)

    new_loop_more_than_2 = get_new_loop_more_than_2(loop_node_more_than_2)

    all_loop_edges_in_one_json_list = find_all_loop_edges_in_one_json_list(json_path)
    dict_loop_node_parent = find_dict_loop_node_parent(all_loop_edges_in_one_json_list)

    json_file_relations = get_json_file_relations(json_path)

    # 把所有的边存下来
    all_loop_nodes_and_parents = []
    all_loop_nodes_and_parents_relation = []

    for i in range(len(json_file_relations)):
        # print(i)
        aa = new_loop_more_than_2[i]  # 输入1.1
        bb = dict_loop_node_parent[i]  # 输入1.2

        # 2) 输出了：[(41, 139), (41, 140), (44, 45), (44, 46), (56, 57), (56, 58)]
        list_loop_node_and_parent_para = find_loop_node_and_parent_para(aa, bb)  # 输入2.1
        all_loop_nodes_and_parents.append(list_loop_node_and_parent_para)

        # print('环中，父节点大于2的节点，所连接的边共{}条，分别为：\n {},：'.format(len(list_loop_node_and_parent_para), list_loop_node_and_parent_para))

        # 3)
        json_file_relations_i = json_file_relations[i]  # 输入2.2

        # 4) 输出了 [135, 135, 124, 124, 124, 124]
        loop_node_category_para = get_loop_node_category_para(list_loop_node_and_parent_para, json_file_relations_i)  # 输入3.2
        # print("loop_node_category_para: ", loop_node_category_para)

        # 5）输出了：[{135: '是_的主体/上级'}, {135: '是_的主体/上级'}, ...]

        relation_file_name = get_relation_file_name(relation_path)  # 输入3.1
        # print("relation_file_name: ", relation_file_name)
        node_parent_relation = find_node_parent_relation_para(relation_file_name, loop_node_category_para)

        all_loop_nodes_and_parents_relation.append(node_parent_relation)

    return all_loop_nodes_and_parents, all_loop_nodes_and_parents_relation


# 【测试】：
# 输入如下：
# relation_path = "../python_test_data/relation.json"
# # json_path = "../python_test_data/json_file/annotation37730-37739.json"
# # json_path = "../python_test_data/json_file/annotation37529-37538.json"
# # json_path = "../python_test_data/json_file/annotation38125-38225.json" # 100个json文件
# # #
# json_path = "../python_test_data/json_file/annotation39469-39530.json"
# all_loop_nodes_and_parents, all_loop_nodes_and_parents_relation = find_all_node_parent_relations(json_path, relation_path)
# print('all_loop_nodes_and_parents: ', all_loop_nodes_and_parents)
# print('------------------------------------------------------------')
# print('all_loop_nodes_and_parents_relation: ', all_loop_nodes_and_parents_relation)


