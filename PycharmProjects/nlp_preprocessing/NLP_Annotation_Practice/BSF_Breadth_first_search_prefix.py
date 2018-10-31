# -*- coding:utf8 -*-
# @TIME : 2018/9/3 下午1:09
# @Author : Allen
# @File : BSF_Breadth_first_search_prefix.py

# 最短路径，两个节点之间的
# 建立图-字典
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

# BSF
def BSF(graph, s):
    queue = []
    seen = set()
    queue.append(s)
    seen.add(s)
    parent = {s: None}

    while (len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                #把这些 key : value 加入字典
                parent[w] = vertex #这些节点就是由vertex分出来的，所以vertex为他们的前一个节点。
        print(vertex)
    # print(parent)
    return parent


parent = BSF(graph, "E")
print("-------------------")
# for key in parent:
#     print(key, parent[key])

# 从B开始出发，找他的前节点，在BFS的基础上，这是最短路径。
v = "B"
while v != None:
    print(v)
    v = parent[v]

