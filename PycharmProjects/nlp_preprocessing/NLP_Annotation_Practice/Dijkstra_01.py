# -*- coding:utf8 -*-
# @TIME : 2018/9/3 下午5:16
# @Author : Allen
# @File : Dijkstra_01.py

import heapq
import math

# 建立图-字典
graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}


def init_distance(graph, s):
    distance = {s: 0}
    for vertex in graph:
        if vertex != s:
            distance[vertex] = math.inf
    return distance


# dijkstra
def dijkstra(graph, s):
    pqueue = []
    seen = set()
    heapq.heappush(pqueue, (0, s))  # 放入数据, 这对点的距离还有名字

    parent = {s: None}
    distance = init_distance(graph, s)

    while (len(pqueue) > 0):
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)

        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]:
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w))
                    parent[w] = vertex  # 这些节点就是由vertex分出来的，所以vertex为他们的前一个节点。
                    distance[w] = dist + graph[vertex][w]
    return parent, distance


parent, distance = dijkstra(graph, "A")

print(parent)
print(distance)
