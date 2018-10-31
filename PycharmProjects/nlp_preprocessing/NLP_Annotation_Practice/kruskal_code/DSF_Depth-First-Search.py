# -*- coding:utf8 -*-
# @TIME : 2018/9/3 上午11:32
# @Author : Allen
# @File : DSF_Depth-First-Search.py

# 建立图-字典
graph = {
    "A": {"B", "C"},
    "B": {"A", "C", "D"},
    "C": {"A", "B", "D", "E"},
    "D": {"B", "C", "E", "F"},
    "E": {"C", "D"},
    "F": {"D"}
}


# 把队列结构改成栈结构就行，弹出队列最后一个‘’
def DFS(graph, s):
    stack = [];
    seen = set();
    stack.append(s)
    seen.add(s)

    while (len(stack) > 0):
        vertex = stack.pop()  # 弹出最后一个元素
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        # print(vertex)
    # print(seen)
    return seen


dfs_result = DFS(graph, "A")
print(dfs_result)
print("------------")
DFS(graph, "E")
