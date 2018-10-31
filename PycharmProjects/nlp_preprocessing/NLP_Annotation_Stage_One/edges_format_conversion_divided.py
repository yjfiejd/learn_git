"""

输入： 一个json文件地址

输入1） 已经修改好的new_graph格式  ->  目的把他们的weight置为零
new_graph_1 = {13: {112: {'weight': 31}}, 27: {123: {'weight': 31}}, 37: {134: {'weight': 31}},
               113: {13: {'weight': 86}, 110: {'weight': 99}, 14: {'weight': 134}}, 18: {17: {'weight': 86}},
               116: {18: {'weight': 86}},}
输入2) 已经找好的图中的所有的子树， -> 通过输入1，形成最终输入格式
tree_set = [{1, 108, 109}, {4, 5, 6, 8, 10, 11, 13, 110, 14, 111, 113, 112},}


输出： right_input, right_input_by_edges

输出1） 每一个子图和它相连的节点式，且格式正确，weight为0
[{109: {108: {'weight': 0}, 1: {'weight': 0}}}, {13: {112: {'weight': 0}]

输出2） 每个子图的中的所有子图，连接的边，的集合。
right_input_by_edges:  [[(57, 58), (1, 57)], [(5, 4),...]

"""


from NLP_Annotation_Stage_One.change_one_json_to_dict import *
from NLP_Annotation_Stage_One.edges_format_conversion import *
from NLP_Annotation_Stage_One.nodes_connected_in_MST import nodes_connected_in_MST, find_nodes_connected_in_MST
from copy import deepcopy
from NLP_Annotation_Stage_One.find_all_edges_with_and_without_weight import *

# 1) 步骤一 ： 为了获得输入一如下：
# graph = [(13, 112, 31), (27, 123, 31), (37, 134, 31), (113, 13, 86), (18, 17, 86), (116, 18, 86), (126, 124, 86)]

# # 2） 步骤二： 为了获得输入二如下：
# # graph_without_weight = [(109, 1), (109, 108), (5, 4), (8, 111), (110, 8), (110, 6), (110, 5), (110, 10), (10, 11)]

# 3） 步骤三，获得最终的输入格式 : [{109: {108: {'weight': 0}, 1: {'weight': 0}}}, ...]
def get_right_input(new_graph, nodes_connected_subtree):
    """
    :param new_graph:  输入带权值的边集合：new_graph 其实是（all_edges_in_graph - with weight）:  {112: {13: {'weight': 31}}, 123: {27: {'weight': 31}}, 134: {37: {'weight': 31}}, 13: {113: {'weight': 86}}
    :param nodes_connected_subtree: 图中的所有的子簇的节点集合：nodes_connected_subtree = [{1, 108, 109}, {4, 5, 6, 8, 10, 11, 13, 110, 14, 111, 113, 112},}
    :return: right_input -> 图字典格式，所有子簇中，节点与父节点集合，'weight'=0 : [{109: {108: {'weight': 0}, 1: {'weight': 0}}}, ...]
    """
    result = []
    test_proto = {}
    # 重置'weight=0'
    for item in new_graph:
        for key in new_graph[item]:
            new_graph[item][key]['weight'] = 0

    # 通过所有的子树，找到他们的父节点
    for item in nodes_connected_subtree:  # 遍历子树 item： {1, 108, 109}
        test = deepcopy(test_proto)
        for i in new_graph:  # 遍历图中所有的key值，每次拿出一个值，12， 113，... 等等
            if i in item:  # 如果i 对应的相连节点都拿出来，over
                test[i] = new_graph[i]  # 放入新的字典
        result.append(test)
    return result

# right_input = get_right_input(new_graph, nodes_connected_subtree)


# 4) 获得right_input中的边的集合：[[(109, 108), (109, 1)], [(13, 112), (113, 13), (113, 110),...]
def get_right_input_by_edges(right_input):
    finnal_result = []
    for item in right_input:  # 进入第一个大括号 -> {109: {108: {'weight': 0}, 1: {'weight': 0}}}
        result = []
        for key in item:  # 进入第二个大括号获得key -> 109
            for sub_item in item[key]:  # 进入第三个大括号 -> 获得sub_item=108， sub_item=109, key为刚才的109
                result.append((key, sub_item))
        finnal_result.append(result)
    return finnal_result


# right_input_by_edges = get_right_input_by_edges(right_input)

# print('\n')
# print('right_input_by_edges: ' , right_input_by_edges)


# 5) 函数：
def find_right_input_edges(json_path):
    """
    :param json_path:  输入一个json文件
    :return: 获得，这个图子图中，所有连接的点，他们的边的集合,
    输出1） ： right_input: [{57: {58: {'weight': 0}}, 1: {57: {'weight': 0}}}, {5: {4: {'weight': 0},...]
    输出2） ： right_input_by_edges:  [[(57, 58), (1, 57)], [(5, 4), (5, 3)], [(7, 6), ...]
    """

    new_graph = weight_edges_to_transform_edges(json_path) # 获得输入1) new_graph:  {13: {112: {'weight': 31}}, 27: {123: {'weight': 31}}...}

    nodes_connected_subtree = find_nodes_connected_in_MST(json_path) # 获得输入2）nodes_connected_subtree:  [{1, 108, 109}, {4, 5, 6, 8, 10, 11, 13, 110, 14, 111, 113, 112}, ...]

    right_input = get_right_input(new_graph, nodes_connected_subtree)  # 获得输出1） 每一个子图和它相连的节点式，且格式正确，weight为0 -> [{109: {108: {'weight': 0},..]

    right_input_by_edges = get_right_input_by_edges(right_input)  # -> [[(109, 108), (109, 1)],..] 最小生成树中的，不带权值的边集合

    return right_input, right_input_by_edges


#【测试】
# json_path = "../python_test_data/json_file/annotation37730-37739.json"
# json_path = "../python_test_data/json_file/annotation37529-37538.json"

# json_path = "../python_test_data/json_file/annotation39469-39530.json"


# right_input = find_right_input_edges(json_path)[0]
# right_input_by_edges = find_right_input_edges(json_path)[1]
# print('right_input = ', right_input)
# print('right_input_by_edges = ', right_input_by_edges)
