# python algorithm _ Kruskal _ Minimum Sapnning

from collections import defaultdict


class Graph:

    # 初始化顶点数，与graph表示集合
    def __init__(self, vertex):
        self.V = vertex  # 节点个数
        self.graph = []  # 定义一个list来存储图

    # 添加边
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # 查找根节点
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # 并查集-判断是否又环，把矮的树放入高的树
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # 定义Kruskal算法
    def KruskalMST(self):

        result = []  # 用于存储最后的最小生成树 -> 边的形式存储
        i = 0  # 图中的第几条边
        e = 0  # 边的个数计数

        # 1) 对边的权值进行排序
        self.graph = sorted(self.graph, key=lambda item: item[2])
        print(self.graph)
        parent = []
        rank = []
        for node in range(self.V):  # 建立子集V，顶点个数
            parent.append(node)
            rank.append(0)

        # 2) 选择最小的边 , 合并2个不在环里的节点，i 递增
        while e < self.V - 1:  # 边的条数应该为顶点个数-1
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            # 如果边不增加环，则把这条边加入result
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("下面是构建的MST的边: ")
        for u, v, weight in result:
            print("%d -- %d 权值：%d" % (u, v, weight))


# g = Graph(4)
# g.addEdge(0, 1, 10)
# g.addEdge(1, 2, 6)
# g.addEdge(0, 3, 5)
# g.addEdge(1, 3, 15)
# g.addEdge(2, 3, 4)

# g.KruskalMST()

g2 = Graph(5)
g2.addEdge(0, 1, 5)
g2.addEdge(0, 4, 2)
g2.addEdge(1, 4, 15)
g2.addEdge(1, 2, 10)
g2.addEdge(4, 3, 6)
g2.addEdge(2, 3, 8)

g2.KruskalMST()
