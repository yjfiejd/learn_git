
"""
# 输入：json 文件  -> 得到原图中已经连接的边 - edges_without_weight :
# [(109, 1), (109, 108), (5, 4), (8, 111), (110, 8), (110, 6), (110, 5), (110, 10), (10, 11), (13, 112)]

# 输出：最小生成树中，各个子树，组成的森林
# [{1, 108, 109}, {4, 5, 6, 8, 10, 11, 13, 110, 14, 111, 113, 112}, {17, 18, 114, 115, 116}】

"""


import networkx as nx
from networkx.algorithms import tree
import matplotlib.pyplot as plt
from NLP_Annotation_Stage_One.find_all_edges_with_and_without_weight import *



def nodes_connected_in_MST(graph_without_weight):
    # 1）创建图对象 networkx -> 添加所有的边
    Test_graph = nx.Graph()
    Test_graph.add_edges_from(graph_without_weight)
    all_nodes_networks = Test_graph.nodes
    len_of_Test_graph = len(Test_graph.nodes)
    all_edges_networks = Test_graph.edges  # <class 'networkx.classes.reportviews.EdgeView'>

    # 可视化
    # nx.draw(Test_graph, with_labels=True, font_weight='bold')
    # plt.show()

    all_edges = []
    for i in all_edges_networks:
        all_edges.append(i)

    # 2） 找到所有相连的子树(原图中）
    sub_tree_nodes = list(nx.connected_components(Test_graph))
    # print("原图中一共有{}簇连接，共计连接{}个node".format(len(sub_tree_nodes), len_of_Test_graph))

    # 3）找到所有的最小生成树 - 用edges表示
    mst = tree.minimum_spanning_edges(Test_graph, algorithm='kruskal', data=False)
    mst_edges = list(mst)  # 最小生成树结果

    # 4) 创建最小生成树子图，并可视化
    G_mst = nx.Graph()
    G_mst.add_edges_from(mst_edges)

    sub_tree_nodes_MST = list(nx.connected_components(G_mst))
    # print("最小生成树一共有{}簇连接, 共计连接{}个node".format(len(sub_tree_nodes_MST), len(G_mst.nodes)))

    return sub_tree_nodes_MST


# 5) 找到all_edges中有，但是mst_edges中缺失的边
def find_diff(A, B):
    """
    其中A是集合的全部连通边，B是最小生成树的边
    """
    diff_edges = []
    for i in A:
        if i not in B:
            diff_edges.append(i)
    return diff_edges

# diff_edges = find_diff(all_edges_networks, mst_edges)


# 主函数
def find_nodes_connected_in_MST(json_path):
    """
    :param json_path:  一个json的地址
    :return: 获得这个图中，所有的最小生成树的子树连接的节点集合
    [{1, 108, 109}, {4, 5, 6, 8, 10, 11, 13, 110, 14, 111, 113, 112},...]
    """
    all_edges_in_graph = find_all_edges_with_and_without_weight(json_path)
    all_edges_without_weight = all_edges_in_graph[1] # 获得edges_without_weight
    nodes_connected_subtree = nodes_connected_in_MST(all_edges_without_weight)
    return nodes_connected_subtree


## 测试数据：

# json_path = "../python_test_data/json_file/annotation37730-37739.json"
# json_path = "../python_test_data/json_file/annotation37529-37538.json"

#
# json_path = "../python_test_data/json_file/annotation39469-39530.json"
#
#
#
# nodes_connected_subtree = find_nodes_connected_in_MST(json_path)
# print("nodes_connected_subtree: ", nodes_connected_subtree)
# print('len(nodes_connected_subtree): ', len(nodes_connected_subtree))

