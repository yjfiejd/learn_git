# # http://www.qttc.net/201302272.html  Python跳出for循环continue与break
# # 代码 错误，并没有找到环
#
#
# def kruskal(graph):
#     assert type(graph) == dict
#
#     nodes = graph.keys()  # 获取所有的keys，node节点
#     visited = set()  # 这是一个不重复的set集合
#     path = []  # 路径
#     next = None  # 下一个指针
#
#     while len(visited) < len(nodes):  # 当visite中具有所有的node了，跳出循环
#         distance = float('inf')  # 初始化距离为无限大
#         for s in nodes:  # 对于每一个node，如果出现了节点不在其中，或者节点相等的，，continue跳过这个继续执行
#             for d in graph[s].keys():
#                 # print(d)
#                 if s in visited and d in visited or s == d:
#                     continue
#                 if graph[s][d] < distance:  # 当s, d的距离小于distance时候，
#                     distance = graph[s][d]  # 更新距离
#                     pre = s  # 更新指出结点
#                     next = d  # 更新指入节点
#
#         path.append((pre, next))  # 更新path路径列表
#         visited.add(pre)  # 更新 visited列表
#         visited.add(next)
#
#     return path
#
#
# if __name__ == '__main__':
#     graph = {
#         "A": {"B": 5, "C": 1},
#         "B": {"A": 5, "C": 2, "D": 1},
#         "C": {"A": 1, "B": 2, "D": 4, "E": 8},
#         "D": {"B": 1, "C": 4, "E": 3, "F": 6},
#         "E": {"C": 8, "D": 3},
#         "F": {"D": 6}
#     }
#     path = kruskal(graph)
#     print(path)
#
#     # print(graph["A"]["C"])