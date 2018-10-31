# -*- coding:utf8 -*-
# @TIME : 2018/9/3 上午10:23
# @Author : Allen
# @File : BSF_Breadth-first search.py

# 建立图-字典
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


# BFS函数,传入两个参数，（图，第一个节点s）
def BFS(graph, s):
    queue = []  # 1)建立一个list列表
    queue.append(s)  # 2)把第一个节点放入
    seen = set()  # pyton里的这个括号代表set，用的是hashset，查找速度快
    seen.add(s)
    while (len(queue) > 0):  # 3)只要队列不为空，每次从队列拿一个节点出来 -> 把它的邻接点放入队列
        vertex = queue.pop(0)  # 拿一个点出来后，
        nodes = graph[vertex]  # 找出了拿出的每个点的邻接点，
        # 4) 如果拿出来的节点，把邻接点nodes中还没有访问过的节点放入队列
        # 5）需要记录一下，哪些节点是已经访问过的
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)
    return seen


bfs_result = BFS(graph, "A")
print(bfs_result)
print('-----------')
BFS(graph, "E")
