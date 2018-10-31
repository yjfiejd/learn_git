"""
输入： 一个json的path ->   all_loop_edges_in_one_json_list  一个json文件中（十段话），每段话中所有的环的list，edges形式

输出： 找到所有环中，父节点大于2个的节点，返回list  或者是 set

"""

import networkx as nx
import matplotlib.pyplot as plt

# 1） 画个图看一看
from NLP_Annotation_Stage_One.find_all_loop_edges_in_one_json import *

def draw_all_loop_one_json(all_loop_edges_in_one_json_list):
    """
    输入：all_loop_edges_in_one_json_list
    输出：画图
    """
    num_1 = 0
    for paragraph_loop in all_loop_edges_in_one_json_list:
        num_2 = 0
        for i in paragraph_loop:
            G_test = nx.DiGraph()
            G_test.add_edges_from(i)
            print('出现环的节点为： ', G_test.nodes)
            plt.figure()
            nx.draw_networkx(G_test)
            a = plt.show()
            num_2 = num_2 + 1
            print('****以上为第', num_1, '段话--中的第', num_2, '个环****')

        print('--------------------以上为第', num_1, '段话中出现的环----------------------\n')
        num_1 = num_1 + 1

    return a


# 2) 10段话中所有的环节点的 -> 找到父节点list， 环节点list
def find_json_node_parent_list(all_loop_edges_in_one_json_list):
    """
    输入：一个json文件中（十段话），每段话中所有的环的list，edges形式
    输出：
    输出1）：每个环中的每个节点的父节点list
    输出2）：每个环，对应的节点list
    """
    json_node_parent_list = []
    nodes_list_1 = []  # 存储节点list for all paragraph
    for paragraph_loop_edges in all_loop_edges_in_one_json_list:  # 进入每一段话
        sentence_node_parent_list = []
        nodes_list_2 = []  # 存储节点list for sentence
        for sentence_loop_edges in paragraph_loop_edges:  # 进入每一个句子，环
            G = nx.DiGraph()
            G.add_edges_from(sentence_loop_edges)
            list_G_nodes = list(G.nodes)  # 获得每个句子的节点
            nodes_list_2.append(list_G_nodes)
            #             print(sentence_loop_edges, '的节点是： ' , list_G_nodes)
            node_parent_list = []
            for one_node in list_G_nodes:
                one_node_parent = G.predecessors(one_node)
                list_a = []
                for i in one_node_parent:
                    list_a.append(i)
                node_parent_list.append(list_a)
            sentence_node_parent_list.append(node_parent_list)
        nodes_list_1.append(nodes_list_2)
        json_node_parent_list.append(sentence_node_parent_list)
    return json_node_parent_list, nodes_list_1


# 3） 构建一个字典，节点node：父节点node_parent
def find_dict_loop_node_parent(all_loop_edges_in_one_json_list):
    """
    输入：all_loop_edges_in_one_json_list，json文件中， -> 10段话，每段话中出现的环，Edges的表示，list
    输出：找到每个环中，节点 - 父节点 组成的list，字典  -> 未来需要 挖出所有的入度大于1的节点
    """
    json_node_parent_list = find_json_node_parent_list(all_loop_edges_in_one_json_list)
    nodes_and_parents = json_node_parent_list[0]  # 获得节点的父节点集合
    nodes = json_node_parent_list[1]  # 获得节点集合

    list_1 = []
    for paragraph_num in range(len(nodes)):  # 进入每一段文字遍历
        nodes_and_parents_1 = nodes_and_parents[paragraph_num]
        nodes_1 = nodes[paragraph_num]
        #     print(nodes_1)
        #     print(nodes_and_parents_1)
        #     print('-------')

        list_2 = []
        for sentence_num in range(len(nodes_1)):
            nodes_and_parents_2 = nodes_and_parents_1[sentence_num]
            nodes_2 = nodes_1[sentence_num]
            #         print(nodes_2)
            #         print(nodes_and_parents_2)
            #         print('******')

            list_3 = []
            for i in range(len(nodes_2)):
                dict_3 = dict(list(zip(nodes_2, nodes_and_parents_2)))
            list_3.append(dict_3)

            list_2.append(list_3)
        list_1.append(list_2)

    return list_1


# 4） 找到所有环中，节点的父节点个数大于2， list
def find_loop_node_more_than_2(json_path):
    """
    输入：all_loop_edges_in_one_json_list
    输出：找到环中，父节点大于2个的节点，返回list
    """

    all_loop_edges_in_one_json_list = find_all_loop_edges_in_one_json_list(json_path)
    dict_loop_node_parent = find_dict_loop_node_parent(all_loop_edges_in_one_json_list)

    list_value_0 = []
    for i in dict_loop_node_parent:
        #     print(i)
        list_value_1 = []
        for kkk in i:
            #         print(kkk)
            list_value_2 = []
            for i in kkk[0]:
                value = kkk[0].get(i)  # 使用get获得字典中的值
                if len(value) > 1:  # 如果value的值的个数大于1
                    list_value_2.append(i)  # 把这个value对应的key取出来
            #         print(list_value_2)
            list_value_1.append(list_value_2)
        list_value_0.append(list_value_1)

    return list_value_0


# 5) 把结果，由list转为set  ->  （目前不需要转为set，整体处理，一段文字一段文字处理就行）
# def find_loop_node_more_than_2_set(json_path):
#     """
#     :param json_path:
#     :return:
#     """
#     all_loop_edges_in_one_json_list = find_all_loop_edges_in_one_json_list(json_path)
#
#     loop_node_more_than_2 = find_loop_node_more_than_2(all_loop_edges_in_one_json_list)
#     set_loop_nodes_more_than_2_set = set()
#     for i in loop_node_more_than_2:
#         for j in i:
#             for k in j:
#                 set_loop_nodes_more_than_2_set.add(k)
#     return set_loop_nodes32_more_than_2_set


#  【测试如下：】
# json_path = "../python_test_data/json_file/annotation37529-37538.json"
# json_path = "../python_test_data/json_file/annotation37730-37739.json"
# set_loop_nodes_more_than_2_list = find_loop_node_more_than_2(json_path)
# print("在一个json中，所有环中父节点大于2的节点分布在: {}段文字中".format(len(set_loop_nodes_more_than_2_list)))
# print("在一个json中，每一段环中父节点大于2的节点分别为: \n {}".format(set_loop_nodes_more_than_2_list))
