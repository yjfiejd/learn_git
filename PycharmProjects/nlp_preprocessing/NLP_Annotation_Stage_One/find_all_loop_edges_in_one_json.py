"""
输入： json文件绝对地址 (包含十段文字)

输出：-> 每段话中所有的环的边的集合，这里是十个集合的list, 【不】带有方向'reverse' 'forward'

all_loop_edges_in_one_json_list:  [[[(139, 41), (138, 139), (138, 140), (140, 41)], ....]

"""

# 思路：
# json_path -> 每一段文字（10段） ->  每一段文字的right_input -> 找到每一段的环，edges集合
from NLP_Annotation_Stage_One.change_one_json_to_dict import *
from NLP_Annotation_Stage_One.edges_format_conversion_divided import get_right_input, weight_edges_to_transform_edges, \
    change_z, get_target_graph, get_right_input_by_edges
from NLP_Annotation_Stage_One.find_all_edges_with_and_without_weight import find_all_edges_with_and_without_weight, \
    find_all_edges_with_and_without_weight_new
from NLP_Annotation_Stage_One.find_all_loop_edges_in_paragraph import get_all_loop_edges_in_paragraph, \
    get_all_loop_edges_in_para, find_nodes_connected_in_MST
from NLP_Annotation_Stage_One.nodes_connected_in_MST import nodes_connected_in_MST


# 主函数如下：
def find_all_loop_edges_in_one_json(json_path):
    """
    :param json_path:  一个json文件地址
    :return: 每段话中所有的环的边的集合，这里是十个集合的list, 带有方向'reverse' 'forward'
    all_loop_edges_in_one_json:  [[[(139, 41, 'reverse'), (138, 139, 'reverse'), (138, 140, 'forward'), (140, 41, 'forward')],
    """

    # 获得 all_graph（包括10个子json）:  [{56: {}, 1: {}, 57: {1: 124}, 58: {57: 121},
    all_graph = all_graph_in_json(json_path)  # 从一个json文件 -> 图的格式（共有10个段落)

    all_loop_edges_in_one_json = []

    for i in range(len(all_graph)):  # json中时十段话，进行遍历

        sub_graph = all_graph[i]  # 第一段中的 graph 的表达

        # 1) 第一段中的 获得 edges_with_weight & edges_without_weight
        all_edges_in_graph = find_all_edges_with_and_without_weight_new(sub_graph)
        all_edges_with_weight = all_edges_in_graph[0]  #带权值 -> [(109, 1, 135), (109, 108, 134), (5, 4, 135)
        all_edges_without_weight = all_edges_in_graph[1]  #不带权值 -> [(109, 1), (109, 108), (5, 4), (8, 111)]...]

        # 2) 为了获得right_input: 条件一 new_graph，条件二 nodes_connected_subtree
        weight_edgew_with_brace = change_z(all_edges_with_weight)  # 1） #append((i, j, {'weight': k}))
        new_graph = get_target_graph(weight_edgew_with_brace)  # 2）0: {1: {'weight':10}, 2: {'weight':6}, 3: {'weight':5}},
        nodes_connected_subtree = nodes_connected_in_MST(all_edges_without_weight)  #3) [{1, 108, 109}, {4, 5, 6, 8, 10, 11, 13, 110, 14, 111, 113, 112},
        # print("nodes_connected_subtree: ", nodes_connected_subtree)

        right_input = get_right_input(new_graph, nodes_connected_subtree)  #[{108: {109: {'weight': 0}}, 1: {109: {'weight': 0}}}, {112: {13: {'weight': 0}},

        # print("right_input: ", right_input)

        all_loop_edges_in_paragraph_list = get_all_loop_edges_in_paragraph(right_input)  #[(139, 41, 'reverse'), (138, 139, 'reverse'), (138, 140, 'forward'), (140, 41, 'forward')],

        all_loop_edges_in_one_json.append(all_loop_edges_in_paragraph_list)

    return all_loop_edges_in_one_json



def find_all_loop_edges_in_one_json_list(json_path):
    """
    :param json_path: 一个json文件 ->  上一个函数的结果 [[[(139, 41, 'reverse'), (138, 139, 'reverse'),...]
    :return: 每段话中所有的环的边的集合，这里是十个集合的list, 【不】带有方向'reverse' 'forward'
    all_loop_edges_in_one_json_list： [[[(139, 41), (138, 139), (138, 140), (140, 41)],...]
    """
    all_loop_edges_in_one_json = find_all_loop_edges_in_one_json(json_path)
    list_all = []
    for item in all_loop_edges_in_one_json:
        list_a = []
        for i in item:
            list_b = []
            for j in i:
                list_b.append((j[0], j[1]))
            list_a.append(list_b)
        list_all.append(list_a)
    return list_all



# 【new】增加一个函数，为了获得1个json_path中的多个小json文件中的，每一篇的簇（边表示）
def find_all_right_input_by_edges(json_path):
    """
    :param json_path:  一个json文件地址(含有多个json文件)
    :return: ，返回包含多个集合的list, list中的每一个元素是 每一篇文章的right_input_by_edges（簇集合）
    [[(6, 445), (446, 445), (723, 445)],
     [(10, 426), (424, 426), (425, 426)],
     [(12, 14), (13, 14)],
     [(16, 428), (428, 427)],
     [(17, 20), (18, 20), (19, 20), (21, 22), (20, 22)],
     [(430, 429), (24, 429)],
     [(431, 25)],
     [(432, 28)],...
    """
    all_graph = all_graph_in_json(json_path)  # 从一个json文件 -> 图的格式（共有10个段落)

    all_right_input_by_edges_list = []

    for i in range(len(all_graph)):  # json中时十段话，进行遍历

        sub_graph = all_graph[i]  # 第一段中的 graph 的表达

        # 1) 第一段中的 获得 edges_with_weight & edges_without_weight
        all_edges_in_graph = find_all_edges_with_and_without_weight_new(sub_graph)
        all_edges_with_weight = all_edges_in_graph[0]
        all_edges_without_weight = all_edges_in_graph[1]

        # 2) 为了获得right_input: 条件一 new_graph，条件二 nodes_connected_subtree
        weight_edgew_with_brace = change_z(all_edges_with_weight)  # 1）
        new_graph = get_target_graph(weight_edgew_with_brace)  # 2）
        nodes_connected_subtree = nodes_connected_in_MST(all_edges_without_weight)  # 3)
        # print("nodes_connected_subtree: ", nodes_connected_subtree)

        right_input = get_right_input(new_graph, nodes_connected_subtree)

        right_input_by_edges = get_right_input_by_edges(right_input)

        all_right_input_by_edges_list.append(right_input_by_edges)

    return all_right_input_by_edges_list





# 【测试如下】：
# 结果如下： [[[(139, 41, 'reverse'), (138, 139, 'reverse'),
# json_path = "../python_test_data/json_file/annotation37529-37538.json"
# json_path = "../python_test_data/json_file/annotation37730-37739.json" # 10个json文件
# json_path = "../python_test_data/json_file/annotation38125-38225.json" # 100个json文件
# all_loop_edges_in_one_json = find_all_loop_edges_in_one_json(json_path)
# print('all_loop_edges_in_one_json: ', all_loop_edges_in_one_json)


# -> [这才是找环的]获得每一篇文章中存在的环，组成集合，【环的集合】
# json_path = "../python_test_data/json_file/annotation39469-39530.json"
# all_loop_edges_in_one_json_list = find_all_loop_edges_in_one_json_list(json_path)
# print('all_loop_edges_in_one_json_list = ', all_loop_edges_in_one_json_list)


#new 测试 10.15 -> 获得每一篇文章的【子簇连接集合】（组成list）
# json_path = "../python_test_data/json_file/annotation39469-39530.json"
# all_right_input_by_edges_list = find_all_right_input_by_edges(json_path)
# print("all_right_input_by_edges_list = ", all_right_input_by_edges_list)



