from collections import defaultdict
from NLP_Annotation_Stage_One.find_all_edges_with_and_without_weight import *


# 【函数目的】将图中所有边的格式，由格式一(输入格式) -> 格式二(输出格式)；

# 输入 -> 格式一：
# graph = [(13, 112, 31), (27, 123, 31), (37, 134, 31), (113, 13, 86), (18, 17, 86), (116, 18, 86), (126, 124, 86),
#          (126, 27, 86), (137, 135, 86), (137, 37, 86)]

# 输出 -> 格式二：
# example = {
#     0: {1: {'weight':10}, 2: {'weight':6}, 3: {'weight':5}},
#     1: {0: {'weight':10}, 3: {'weight':15}},
#     2: {0: {'weight':6}, 3: {'weight':4}},
#     3: {0: {'weight':5}, 1: {'weight':15}, 2: {'weight':4}}
# }


# 1) 步骤一：把i, j, k位置的k位置加上weight, 新的格式， 这里的graph指有向边集合
def change_z(graph):
    new_graph = []
    for i, j, k in graph:
        new_graph.append((i, j, {'weight': k}))
    return new_graph


# 2） 步骤二：形成key：value格式，利用工厂方法：defaultdict, 这里的graph指有向边集合
def get_target_graph(graph):
    final_dict = defaultdict(dict)
    for start_point, end_point, weight in graph:
        final_dict[start_point].update({end_point: weight})
    return final_dict


# 3） 组合前两个函数（主函数）
# def graph_transform(graph):
#     new_graph = change_z(graph)
#     final_dict = get_target_graph(new_graph)
#     return final_dict


# 主函数
def weight_edges_to_transform_edges(json_path):
    """
    :param json_path:  输入一个json文件地址 -> 得到weight_edges的集合
    :return: 输出转换后的格式 { 0: {1: {'weight':10}, 2: {'weight':6}, 3: {'weight':5}},...}
    """
    all_edges_in_graph = find_all_edges_with_and_without_weight(json_path)
    weight_edges = all_edges_in_graph[0] # 0）获得有向边的集合 -> 作为输入

    weight_edgew_with_brace = change_z(weight_edges)  # 1）

    final_dict = get_target_graph(weight_edgew_with_brace)  # 2）

    return final_dict




# 【测试】

# json_path = "../python_test_data/json_file/annotation37730-37739.json"
# json_path = "../python_test_data/json_file/annotation37529-37538.json"

# json_path = "../python_test_data/json_file/annotation39469-39530.json"
#
#
# new_graph = weight_edges_to_transform_edges(json_path)
# print('weight_edges_to_transform_edges = ', new_graph)
