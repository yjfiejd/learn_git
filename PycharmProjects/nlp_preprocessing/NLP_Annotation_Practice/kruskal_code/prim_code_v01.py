graph1 = {
    0: {1: 10, 2: 6, 3: 5},
    1: {0: 10, 3: 15},
    2: {0: 6, 3: 4},
    3: {0: 5, 1: 15, 2: 4}
}

graph3 = {
    "A": {"B": 7, "D": 5},
    "B": {"A": 7, "C": 8, "D": 9, "E": 7},
    "C": {"B": 8, "E": 5},
    "D": {"A": 5, "B": 9, "E": 15, "F": 6},
    "E": {"B": 7, "C": 5, "D": 15, "F": 8, "G": 9},
    "F": {"D": 6, "E": 8, "G": 11},
    "G": {"E": 9, "F": 11}
}

from collections import defaultdict
from heapq import *


# 获得所有的节点
def get_all_nodes(graph):
    all_nodes = []
    for node in graph:
        all_nodes.append(node)
    return all_nodes


all_nodes = get_all_nodes(graph1)
print("所有的节点为,共有{}个节点：\n{}".format(len(all_nodes), all_nodes))


# 获得所有的边
def get_all_edges(graph):
    all_edges = []
    for source in graph:
        for target in graph[source].keys():
            all_edges.append((source, target, graph[source][target]))
    return all_edges


all_edges = get_all_edges(graph1)
print("所有的边为,共有{}条边：\n{}".format(len(all_edges),all_edges))


# 传入所有的顶点，所有的边, 利用堆排序, heapq
def prim(vertex, edges):
    adjacent_vertex = defaultdict(list)  # 变成一个有格式的dict, key,list
    for v1, v2, length in edges:
        adjacent_vertex[v1].append((v1, v2, length))
        adjacent_vertex[v2].append((v2, v1, length))
    # print(adjacent_vertex)

    mst = []
    seen = set().add(vertex[0])  # 选择第一个顶点

    adjacent_vertex_edges = adjacent_vertex[vertex[0]]
    # print(adjacent_vertex_edges)

    heapify(adjacent_vertex_edges)  # 将转为堆， 堆排序

    while adjacent_vertex_edges:
        v1, v2, w = heappop(adjacent_vertex_edges)  # 利用堆结构，弹出了最小的边值,比如D
        print(v1, v2)
        if v2 not in seen:
            seen.add(v2)
            mst.append((v1, v2, w))

            for next_vertex in adjacent_vertex[v2]:  # 找到与D相邻的点，如果没有在Heap中， 则被压入heappush
                if next_vertex[2] not in seen:
                    heappush(adjacent_vertex_edges, next_vertex)
    return mst


a = prim(all_nodes, all_edges)
a_len = len(a)
print("最小生成树的结果为，共有{}边：\n{}".format(a_len,a))
