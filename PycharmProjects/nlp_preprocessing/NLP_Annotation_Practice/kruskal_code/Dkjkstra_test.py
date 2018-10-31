# 最短路径算法，是基于BFS的基础上修改的
# 数据结构替换：队列 -> 优先队列

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
    for vertex in graph:  # 将其他的节点距离初始化为正无穷
        if vertex != s:
            distance[vertex] = math.inf
    return distance


def dijkstra(graph, s):
    pqueue = []  # 定义一个优先队列 heapq
    seen = set()  # 定义一个已看set（）
    heapq.heappush(pqueue, (0, s))  # 插入节点&距离，距离写在第一位，节点写在第二位
    # seen.add(s) #这里与BFS不同，最短路径算法中，只有当节点从优先队列中拿出时候才算看过

    parent = {s: None}  # 父节点（parent节点）
    distance = init_distance(graph, s)  # 当前节点到起始点的距离, 除了把初始点距离修改为0， 其他点距离修改为正无穷

    while (len(pqueue) > 0):
        pair = heapq.heappop(pqueue)  # 注意弹出的方法，弹出的东西有2个，一个是点，一个是距离
        dist = pair[0]
        vertex = pair[1]

        seen.add(vertex)  # 当节点被拿出来了才能记为seen

        nodes = graph[vertex].keys()  # 需要添加.keys()才能拿到相邻的节点

        for w in nodes:
            if w not in seen:  # 再把邻接点放入优先队列之前需要当前节点与起始位置的距离
                # 如果发现新放入节点与邻接节点距离+原有距离  < distance[w]
                if dist + graph[vertex][w] < distance[w]:
                    # 插入这个新的点
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w))
                    # 这个点w的父节点是vertex
                    parent[w] = vertex
                    # 把距离需要更新一下，选择更短的那个
                    distance[w] = dist + graph[vertex][w]

    return parent, distance


parent, distance = dijkstra(graph, "A")

print(parent)
print(distance)

