from NLP_Annotation_Stage_One.change_one_json_to_dict import all_graph_in_json
from python_test_data.json_file.build_graph_code import from_json_to_graph


# 注意这里输入一个json文件，但是只会输出第一个对应的图的结果
def get_json_graph(json_path):
    """
    :param json_path: 输入一个json文件路径
    :return: 得到由转化后的图的格式，graph ->  字典格式 {56: {}, 1: {57: 124}, 57: {58: 121}, 58: {}...]
    """
    # 采用原来的 build_graph_code
    # json_graph = from_json_to_graph(json_path)  # 导入build_graph_code中的处理函数

    # 采用更新版本 change_one_json_to_dict, 注意，这里所有的处理都是json里面的第一段话
    all_graph = all_graph_in_json(json_path)
    json_graph = all_graph[0]

    return json_graph


# 主函数
def find_all_edges_with_and_without_weight(json_path):
    """
    :输入：输入一个json文件路径
    :输出: 图中所有的边 （2个输出部分）
    输出1）：# 带权值 -> [(109, 1, 135), (109, 108, 134), (5, 4, 135), (8, 111, 138)...]
    输出2）：# 不带权值 -> [(109, 1), (109, 108), (5, 4), (8, 111)]...]
    """

    graph = get_json_graph(json_path)
    # print("graph_from_json_file :", graph)

    all_edges_with_weight = []
    all_edges_without_weight = []
    for vertice in graph:
        for target in graph[vertice].keys():
            all_edges_with_weight.append((vertice, target, graph[vertice][target]))
            all_edges_without_weight.append((vertice, target))
        all_edges_with_weight = sorted(all_edges_with_weight, key=lambda all_edges_with_weight: all_edges_with_weight[2])  # 排个序而已
    return all_edges_with_weight, all_edges_without_weight


# 【新增】这个函数目的就是 -> 在find_all_loop_edges_in_one_json中需要引用，输入是graph，不是json
def find_all_edges_with_and_without_weight_new(graph):
    """
    :param graph: 获得的一个json中，某段话中的，graph格式
    :return: 也是输出2个东西
    输出1）：# 带权值 -> [(109, 1, 135), (109, 108, 134), (5, 4, 135), (8, 111, 138)...]
    输出2）：# 不带权值 -> [(109, 1), (109, 108), (5, 4), (8, 111)]...]
    """
    all_edges_with_weight = []
    all_edges_without_weight = []
    for vertice in graph:
        for target in graph[vertice].keys():
            all_edges_with_weight.append((vertice, target, graph[vertice][target]))
            all_edges_without_weight.append((vertice, target))
        all_edges_with_weight = sorted(all_edges_with_weight, key=lambda all_edges_with_weight: all_edges_with_weight[2])  # 排个序而已
    return all_edges_with_weight, all_edges_without_weight

# 【测试】

# json_path = "../python_test_data/json_file/annotation37730-37739.json"
# json_path = "../python_test_data/json_file/annotation37529-37538.json"
# json_path = "../python_test_data/json_file/annotation39469-39530.json"

# all_edges_in_graph = find_all_edges_with_and_without_weight(json_path)
# print('all_edges_in_graph_with_weight: ', all_edges_in_graph[0])
# print('all_edges_in_graph_without_weight: ', all_edges_in_graph[1])


