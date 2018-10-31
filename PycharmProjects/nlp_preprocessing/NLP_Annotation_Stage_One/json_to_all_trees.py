"""
输入：一个json的绝对路径：

输出：这个json中共10段文字，每段文字形成的所有的树结构的集合，list格式  ——> ( 由于存在环，部分子图存在多条路径 )
[[EdgeView([(108, 109), (1, 109)])], [EdgeView([(112, 13), (13, 113), (110, 113), (110, 10), (110, 6), (110, 8), (110, 5), (11, 10), (8, 111), (14, 113), (4, 5)])], [EdgeView([(17, 18), (17, 115), (18, 116), (114, 115)])], [EdgeView([(123, 27), (27, 126), (124, 126), (121, 126), (121, 122), (121, 119), (121, 120), (121, 118), (25, 122), (125, 126), (117, 118)])], [EdgeView([(134, 37), (37, 137), (135, 137), (132, 137), (132, 34), (132, 128), (132, 32), (132, 131), (132, 189), (35, 34), (32, 129), (131, 130), (136, 137), (127, 189), (186, 189)])], [EdgeView([(187, 188)])], [EdgeView([(141, 143), (142, 143), (138, 139), (138, 140), (139, 41), (41, 143)]), EdgeView([(141, 143), (142, 143), (138, 139), (139, 41), (140, 41), (41, 143)]), EdgeView([(141, 143), (142, 143), (138, 140), (139, 41), (140, 41), (41, 143)]), EdgeView([(141, 143), (142, 143), (138, 139), (138, 140), (140, 41), (41, 143)])], [EdgeView([(144, 191), (44, 191), (44, 45), (44, 46), (44, 48), (47, 45), (49, 48), (145, 191), (51, 191)]), EdgeView([(144, 191), (44, 191), (44, 45), (44, 46), (44, 48), (47, 46), (49, 48), (145, 191), (51, 191)]), EdgeView([(144, 191), (44, 191), (44, 46), (44, 48), (47, 45), (47, 46), (49, 48), (145, 191), (51, 191)]), EdgeView([(144, 191), (44, 191), (44, 45), (44, 48), (47, 45), (47, 46), (49, 48), (145, 191), (51, 191)])], [EdgeView([(54, 151), (148, 151), (150, 151), (150, 149), (192, 151)])], [EdgeView([(152, 193), (56, 60), (56, 57), (56, 58), (60, 193), (60, 61), (59, 57), (62, 61), (153, 193), (64, 193)]), EdgeView([(152, 193), (56, 60), (56, 57), (56, 58), (60, 193), (60, 61), (59, 58), (62, 61), (153, 193), (64, 193)]), EdgeView([(152, 193), (56, 60), (56, 58), (60, 193), (60, 61), (59, 57), (59, 58), (62, 61), (153, 193), (64, 193)]), EdgeView([(152, 193), (56, 60), (56, 57), (60, 193), (60, 61), (59, 57), (59, 58), (62, 61), (153, 193), (64, 193)])], [EdgeView([(67, 155), (66, 155)])], [EdgeView([(70, 71), (185, 71)])], [EdgeView([(74, 73), (76, 75), (75, 72), (72, 73)])], [EdgeView([(162, 161), (161, 195), (157, 79), (79, 195), (79, 156), (159, 195), (159, 158), (194, 195), (77, 78), (78, 195)])], [EdgeView([(163, 166), (164, 166), (165, 166), (83, 84), (84, 166), (85, 166)])], [EdgeView([(167, 169), (170, 169), (168, 169), (88, 89), (89, 169)])], [EdgeView([(175, 176), (175, 174), (176, 196), (172, 173), (173, 174)])], [EdgeView([(101, 181), (179, 180), (180, 181), (100, 181)])], [EdgeView([(104, 184), (182, 183), (183, 184)])]]

"""


from NLP_Annotation_Stage_One.change_one_json_to_dict import *
from NLP_Annotation_Stage_One.edges_format_conversion import find_all_edges_with_and_without_weight_new, change_z, get_target_graph
from NLP_Annotation_Stage_One.edges_format_conversion_divided import get_right_input
from NLP_Annotation_Stage_One.generate_all_trees_in_subgraph import generate_all_trees_in_subgraph
from NLP_Annotation_Stage_One.nodes_connected_in_MST import nodes_connected_in_MST



def json_to_all_trees(json_path):
    """
    :param json_path: 一个json文件地址
    :return:
    """
    all_graph = all_graph_in_json(json_path)  # 从一个json文件 -> 图的格式 (这里一共有10个段落)

    all_trees_in_json = []

    for i in range(len(all_graph)):  # 获得第一个段落 subgraph

        sub_graph = all_graph[i]  # 第一段中的 graph 的表达

        # 1) 第一段中的 获得 edges_with_weight & edges_without_weight
        all_edges_in_graph = find_all_edges_with_and_without_weight_new(sub_graph)
        all_edges_with_weight = all_edges_in_graph[0]
        all_edges_without_weight = all_edges_in_graph[1]

        # 2) 为了获得right_input: 条件一 new_graph，条件二 nodes_connected_subtree
        weight_edgew_with_brace = change_z(all_edges_with_weight)  # 1）
        new_graph = get_target_graph(weight_edgew_with_brace)  # 2）
        nodes_connected_subtree = nodes_connected_in_MST(all_edges_without_weight)  # 3)

        right_input = get_right_input(new_graph, nodes_connected_subtree)

        all_trees_in_subgraph = generate_all_trees_in_subgraph(right_input)  # 获得这个段落图中，所有的生成树

        all_trees_in_json.append(all_trees_in_subgraph)  # 把所有子树的结果放入[] 进行保存

    return all_trees_in_json


# 【测试开始】:

# json_path = "../python_test_data/json_file/annotation37529-37538.json"
# all_trees_in_json = json_to_all_trees(json_path)
#
# # 找出了第一段文字中所有的子图，形成的所有树。
# all_trees_in_json_01 = all_trees_in_json[0]
# print('all_trees_in_json_01: ', all_trees_in_json_01)
