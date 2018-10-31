"""
输入： json中的某一段话中，right_input -> 处理好的标准输入格式  ->  【right_input用处1：一条路：找出一段话中所有的树】// 【right_input用处2：找到这段话中所有的环的，edges，后续需要分析】

[{109: {108: {'weight': 0}, 1: {'weight': 0}}},
 {13: {112: {'weight': 0}},
  113: {13: {'weight': 0}, 110: {'weight': 0}, 14: {'weight': 0}},
  10: {11: {'weight': 0}},
  110: {10: {'weight': 0},
   8: {'weight': 0},
   6: {'weight': 0},
   5: {'weight': 0}},
  5: {4: {'weight': 0}},
  8: {111: {'weight': 0}}},...]

输出： 返回一个list， 找到所有的环组成的有向边，forward表示环画圈的方向，reverse 表示这里的方向与原来有向图方向不同
[
[(41, 139, 'forward'),
 (139, 138, 'forward'),
 (140, 138, 'reverse'),
 (41, 140, 'reverse')]，

 [(44, 45, 'forward'),
 (45, 47, 'forward'),
 (46, 47, 'reverse'),
 (44, 46, 'reverse')]
]


"""

import networkx as nx
import matplotlib.pyplot as plt
from NLP_Annotation_Stage_One.edges_format_conversion_divided import *

# 1） 获得初始的输入，right_input

# 2)  获得right_input_by_edges， 修改right_input格式，变为每簇中-所有边的集合
def get_right_input_by_edges(right_input):
    finnal_result = []
    for item in right_input:  # 进入第一个大括号 -> {109: {108: {'weight': 0}, 1: {'weight': 0}}}
        result = []
        for key in item:  # 进入第二个大括号获得key -> 109
            for sub_item in item[key]:  # 进入第三个大括号 -> 获得sub_item=108， sub_item=109, key为刚才的109
                result.append((key, sub_item))
        finnal_result.append(result)  # 注意使用append
    return finnal_result


# 3) 获得right_input_list, 变为图中所有边的集合，不考虑属于哪一簇
def get_right_input_list(right_input_by_edges):
    right_input_list = []
    for i in right_input_by_edges:
        result = []
        for j in i:
            result.append(j)
        right_input_list.extend(result)  # 注意使用extend
    return right_input_list


# 4) 画图函数，把每一个子簇的图形画出
def subtree_pictures_in_paragraph(right_input_by_edges):
    for i in right_input_by_edges:
        print(i)
        G = nx.DiGraph()  # 定义有向图，图形
        G.add_edges_from(i)  # 添加边
        plt.figure(figsize=(12, 12))  # 定义画布大小
        nx.draw_networkx(G, with_labels=True)
        sub_picture = plt.show()
    return sub_picture


# 5）
# 返回 all_loop_edges_in_paragraph, 对每段话中的每一簇寻找环
def get_all_loop_edges_in_paragraph(right_input):

    right_input_by_edges = get_right_input_by_edges(right_input)
    all_loop_edges_in_paragraph_list = []
    for sub_tree in right_input_by_edges:
        G_sub_tree = nx.DiGraph()
        G_sub_tree.add_edges_from(sub_tree)
        try:
            sub_tree_loop_edges = list(nx.find_cycle(G_sub_tree, orientation='ignore'))  # 找到每句话中所有的环，的边
            all_loop_edges_in_paragraph_list.append(sub_tree_loop_edges)  # 加入list
        except:
            pass
    return all_loop_edges_in_paragraph_list



# 6）主函数如下
def get_all_loop_edges_in_para(json_path):
    """
    :param json_path:  一个json文件地址
    :return: 返回一个list， 一段话中，找到的所有的环组成的有向边，集合：[[(41, 139, 'forward'), (139, 138, 'forward'), (140, 138, 'reverse'),
    """
    right_input = find_right_input_edges(json_path)[0]  # 获得right_input
    all_loop_edges_in_paragraph_list = get_all_loop_edges_in_paragraph(right_input)
    return all_loop_edges_in_paragraph_list




#【测试】
# json_path = "../python_test_data/json_file/annotation37529-37538.json"

# json_path = "../python_test_data/json_file/annotation39469-39530.json"
#
# all_loop_edges_in_para = get_all_loop_edges_in_para(json_path)
# print('all_loop_edges_in_para: ',all_loop_edges_in_para)

