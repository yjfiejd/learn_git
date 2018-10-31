"""
输入：
:param json_path: 整个json的文件路径（包含多个子json）
:param relation_path: 关系文件

输出：
:return: 所有子json中的
new_paragrapher_cluster_without_label -> 所有子json中删除高层关系够剩下的边 json_cluster_without_label_list =  [[[(6, 445), (446, 445), (723, 445)],
selected_del_edges_list -> 所有子json中删除的是那些高层关系 json_selected_del_edges_list =  [[[('(不借助知识等信息无法具体化)有相关', (30, 434))], [('（远程）是_所承接的主体', (36, 437))],
"""


import networkx as nx
from networkx.algorithms import tree
import matplotlib.pyplot as plt
import pandas as pd
import copy

from NLP_Annotation_Stage_One.find_all_loop_edges_category_text_in_one_jsonfile import \
    find_all_right_input_by_edges_list_category
from NLP_Annotation_Stage_One.find_all_loop_edges_in_one_json import find_all_right_input_by_edges



# # # 1） 获得json中每一篇文章的，子簇，edges （这里抓了10篇json）  -> [[[(6, 445), (446, 445), (723, 445)], [(10, 426), (424, 426),...
# # all_right_input_by_edges_list = find_all_right_input_by_edges(json_path) # 这一步其实不需要
#
# # 2) 获得json中每一篇文章的，子簇（带标签），edges （这里抓了10篇json）  -> [[[{(6, 445): {86: '是_的限定'}}, {(446, 445): {121: '是_的描述/值'}},
# all_right_input_by_edges_list_with_category = find_all_right_input_by_edges_list_category(json_path, relation_path)
#
# # 2.5）<取出了第一篇文章中的带标签子簇 - 子json> (这里抓了1篇json)
# paragrapher_cluster = all_right_input_by_edges_list_with_category[11]


# 3）统计每种关系出现的次数
def summarizing_relations_types_counts(paragrapher_cluster):
    """
    输入： paragrapher_cluster一个子json中带标签的子簇 -> [[{(6, 445): {86: '是_的限定'}}, {(446, 445): {121: '是_的描述/值'}},...
    输出： 汇总这个子json中，各种关系的次数统计  -> edges_category_counts_list :  [('是_的形容', 85), ('是_的主体/上级', 81), ('是_的描述/值', 74),
    """
    paragrapher_cluster_list = []  # 把每一条标签 -> 取出：
    for item in paragrapher_cluster:
        for j in item:
            a = list(j.values())[0]
            b = list(a.values())[0]
            paragrapher_cluster_list.append(b)

    df = pd.DataFrame(paragrapher_cluster_list)
    edges_category_counts = df[0].value_counts()
    edges_category_counts_value = edges_category_counts.tolist()
    edges_category_counts_index = edges_category_counts.index.tolist()
    edges_category_counts_list = list(zip(edges_category_counts_index, edges_category_counts_value))
    return edges_category_counts_list


# 4) 开始删除 high-level 关系
def del_high_level_ralations_in_one_para(paragrapher_cluster):
    """
    输入： paragrapher_cluster一个子json中带标签的子簇 -> [[{(6, 445): {86: '是_的限定'}}, {(446, 445): {121: '是_的描述/值'}},...
    输出： 共2个
    第一个为：new_paragrapher_cluster_with_label ->   删除了高层关系后的子簇集合（带标签） ->  [[{(473, 474): {86: '是_的限定'}}], [{(5, 7): {86: '是_的限定'}}, {(6, 7): {86: '是_的限定'}}],
    第二个为：selected_del_edges_list 删除的边的集合 -> [('(不借助知识等信息无法具体化)有相关', (30, 434)), [('（远程）是_所承接的主体', (36, 437))],
    """
    new_paragrapher_cluster_with_label = []
    record_list_all = []
    for each_cluster in paragrapher_cluster:
        record_list_1 = []
        record_list_2 = []
        record_list_3 = []
        record_list_4 = []
        each_cluster_copy = copy.deepcopy(each_cluster)  # 注意使用深度拷贝，list_remove 很坑
        for edge in each_cluster:
            if list(list(edge.values())[0].values())[0] == '(形容词上级词数词等)指代了前面某复数物体的一部分':
                target_edge_4 = list(edge.keys())[0]
                # print("（'(形容词上级词数词等)指代了前面某复数物体的一部分'_edges: ", target_edge_4)
                record_list_4.append(('(形容词上级词数词等)指代了前面某复数物体的一部分', target_edge_4))
                # 注意删除的时候删除原list，不要删除备份list，这样会改变备份list中的下标。采用deepcopy方式，解决该问题，在原来的一个list
                each_cluster_copy.remove({list(edge.keys())[0]: list(edge.values())[0]})

            elif list(list(edge.values())[0].values())[0] == '(不借助知识等信息无法具体化)有相关':
                target_edge = list(edge.keys())[0]
                # print("(不借助知识等信息无法具体化)有相关_edge: ", target_edge)
                record_list_1.append(('(不借助知识等信息无法具体化)有相关', target_edge))
                each_cluster_copy.remove({list(edge.keys())[0]: list(edge.values())[0]})

            elif list(list(edge.values())[0].values())[0] == '（远程）是_所承接的主体':
                target_edge_2 = list(edge.keys())[0]
                # print("（远程）是_所承接的主体_edges: ", target_edge_2)
                record_list_2.append(('（远程）是_所承接的主体', target_edge_2))
                each_cluster_copy.remove({list(edge.keys())[0]: list(edge.values())[0]})

            elif list(list(edge.values())[0].values())[0] == '(指代词)指代了_[严格相等]':
                target_edge_3 = list(edge.keys())[0]
                # print("(指代词)指代了_[严格相等]_edges: ", target_edge_3)
                record_list_3.append(('(指代词)指代了_[严格相等]', target_edge_3))
                each_cluster_copy.remove({list(edge.keys())[0]: list(edge.values())[0]})
        new_paragrapher_cluster_with_label.append(each_cluster_copy)
        record_list_all.append(record_list_1)
        record_list_all.append(record_list_2)
        record_list_all.append(record_list_3)
        record_list_all.append(record_list_4)
    # 提取出需要的部分，去除空集合。
    selected_del_edges_list = []
    for i in record_list_all:
        if len(i):
            selected_del_edges_list.append(i)
    return new_paragrapher_cluster_with_label, selected_del_edges_list


# 5） 【去除标签】带标签的簇edges -> 不带标签的簇edges
def recover_del_edges_cluster_format(paragrapher_cluster_with_label):
    """
    :输入：一个带标签的，paragrapher_cluster_with_label ->  [[{(446, 445): {121: '是_的描述/值'}}, {(723, 445): {121: '是_的描述/值'}}],...
    :输出: 返回一个不带标签的，子json，簇 -> [[(446, 445), (723, 445)],...
    """
    paragrapher_cluster_without_label = []
    for each_cluster in paragrapher_cluster_with_label:
        list_1 = []
        for each_cluster_edge in each_cluster:
            list_1.append(list(each_cluster_edge.keys())[0])
        paragrapher_cluster_without_label.append(list_1)
    return paragrapher_cluster_without_label



# 6） 【主函数】，处理整个json_path中所有的子json

def find_new_paragrapher_cluster_without_label_in_all_json(json_path, relation_path):
    """
    :param json_path: 整个json的文件路径（包含多个子json）
    :param relation_path: 关系文件
    :return: 所有子json中的
    new_paragrapher_cluster_without_label -> 所有子json中删除高层关系够剩下的边 json_cluster_without_label_list =  [[[(6, 445), (446, 445), (723, 445)],
    selected_del_edges_list -> 所有子json中删除的是那些高层关系 json_selected_del_edges_list =  [[[('(不借助知识等信息无法具体化)有相关', (30, 434))], [('（远程）是_所承接的主体', (36, 437))],
    """
    # 1) 获得json中每一篇文章的，子簇（带标签），edges （这里抓了10篇json）  -> [[[{(6, 445): {86: '是_的限定'}}, {(446, 445): {121: '是_的描述/值'}},
    all_right_input_by_edges_list_with_category = find_all_right_input_by_edges_list_category(json_path, relation_path)
    # 2）定义容器，准备遍历所有的子json
    json_cluster_without_label_list = [] #容器1
    json_selected_del_edges_list = [] # 容器2
    for i in range(len(all_right_input_by_edges_list_with_category)):
        # 获得每一个子 json
        paragrapher_cluster = all_right_input_by_edges_list_with_category[i]
        # 2.1）获得 新的子json中的子簇（edegs）表达形式 - 带标签
        # [[{(6, 445): {86: '是_的限定'}}, {(446, 445): {121: '是_的描述/值'}},
        new_paragrapher_cluster_with_label = del_high_level_ralations_in_one_para(paragrapher_cluster)[0]
        # 2.1）获得 新的子json中的子簇（edegs）表达形式 - 不带标签
        # [[(6, 445), (446, 445), (723, 445)], [(10, 426), (424, 426),
        new_paragrapher_cluster_without_label = recover_del_edges_cluster_format(new_paragrapher_cluster_with_label)
        json_cluster_without_label_list.append(new_paragrapher_cluster_without_label)
        # 2.2）获得 寻找到的需要删除的边
        # [[('(不借助知识等信息无法具体化)有相关', (30, 434))], [('（远程）是_所承接的主体', (36, 437))]
        selected_del_edges_list = del_high_level_ralations_in_one_para(paragrapher_cluster)[1]
        json_selected_del_edges_list.append(selected_del_edges_list)
    return json_cluster_without_label_list, json_selected_del_edges_list






# new 测试：

# relation_path = "/Users/synyi/PycharmProjects/NLP_Annotation_Practice/python_test_data/relation.json"
# json_path = "../python_test_data/json_file/annotation39469-39530.json"
# json_path = "../python_test_data/json_file/annotation37529-37538.json"

# json_cluster_without_label_list, json_selected_del_edges_list = find_new_paragrapher_cluster_without_label_in_all_json(json_path, relation_path)
#
# print("json_cluster_without_label_list = ", json_cluster_without_label_list)
# print('-----------------------------------')
# print("json_selected_del_edges_list = ", json_selected_del_edges_list)
# print('-----------------------------------')











# old 测试：
# # 获得这个子json中的，边信息的统计结果
# # [('是_的形容', 85), ('是_的主体/上级', 81), ('是_的描述/值', 74), ('是_的限定', 72),
# edges_category_counts_list = summarizing_relations_types_counts(paragrapher_cluster)
# print("edges_category_counts_list  = ", edges_category_counts_list)
# print('-------------------------------')
#
# # 获得 寻找到的需要删除的边
# # [[('(不借助知识等信息无法具体化)有相关', (30, 434))], [('（远程）是_所承接的主体', (36, 437))],
# selected_del_edges_list = del_high_level_ralations_in_one_para(paragrapher_cluster)[1]
# print("selected_del_edges_list = ", selected_del_edges_list)
# print('-------------------------------')
#
# # 获得 新的子json中的子簇（edegs）表达形式 - 带标签
# # [[{(6, 445): {86: '是_的限定'}}, {(446, 445): {121: '是_的描述/值'}},
# new_paragrapher_cluster_with_label = del_high_level_ralations_in_one_para(paragrapher_cluster)[0]
# print("new_paragrapher_cluster_with_label = ", new_paragrapher_cluster_with_label)
# print('-------------------------------')
#
# # 获得 新的子json中的子簇（edegs）表达形式 - 不带标签
# # [[(6, 445), (446, 445), (723, 445)], [(10, 426), (424, 426),
# new_paragrapher_cluster_without_label = recover_del_edges_cluster_format(new_paragrapher_cluster_with_label)
# print("new_paragrapher_cluster_without_label = ", new_paragrapher_cluster_without_label)
# print('-------------------------------')
