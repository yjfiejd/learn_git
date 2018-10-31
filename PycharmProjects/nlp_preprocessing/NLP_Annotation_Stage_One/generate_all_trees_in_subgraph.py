import yamada
import networkx as nx


def generate_all_trees_in_subgraph(right_input):
    """
    :param right_input:  1个json文件中其中一段, 获得的right_input
    :return:  返回这段话中，连通的子图中所有的生成树（基于Yamada 算法中的最小生成树）
    [[EdgeView([(108, 109), (1, 109)])], [EdgeView([(112, 13), (13, 113), (110, 113), (110, 10), (110, 6), (110, 8),...]
    """
    # 取出每个子图，找出所有的树
    # print('right_input: ',right_input)
    all_trees_in_subgraph = []
    for i in right_input:
        graph = nx.Graph(i)
        # retrieve all minimum spanning trees
        graph_yamada = yamada.Yamada(graph)
        all_msts = graph_yamada.spanning_trees()

        # # 把每个子图中所有的树打印出来
        list_b = []
        for i in all_msts:
            a = i.edges()
            list_b.append(a)
        all_trees_in_subgraph.append(list_b)  # 注意加上，.edges(), 注意这里用了2个list, append
    return all_trees_in_subgraph

# all_trees_in_subgraph = generate_all_trees_in_subgraph(right_input)
# print("\n")
# print('all_trees_in_subgraph: ', all_trees_in_subgraph)
