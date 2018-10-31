from inspect import isgeneratorfunction

graph_2 = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}


class Graph(dict):


    def weight(self, edge):
        """
        11）:param edge: 给一条边
        :return: 输出它的权重
        """
        if edge.source in self and edge.target in self[edge.source]:
            return self[edge.source][edge.target].weight
        else:
            return 0

    def iternodes(self):
        """
        12）:return:把图中所有的节点拿出来
        """
        return self.keys()  # 方法二：强制转换为list格式，list(self.keys())


    def iteroutedges(self, source):
        """
        14）:return: 返回outedges,图中的 -> 由source指向target 的权值 -> 找到那些由source指出去的权值（类别）
        """
        for target in self[source]:
            yield self[source][target]


    def show(self):
        """
        :return: 把图打印出来
        """
        for source in self.iternodes():
            print("{} :".format(source))
            for edge in self.iteroutedges(source):
                print(edge)
                print("{} ({})".format(edge.target, edge.weight))
                # if edge.weight == 1:
                #     print(edge.target)
                # else:
                #     print("{} ({})".format(edge.target, edge.weight))



b = Graph(graph_2)


print('-----------------------------')
# 测试节点是否能够全部打印
print("所有的节点为：{}".format(b.iternodes()))
print("与source节点C相连的邻接边与权值是{}".format(b["C"]))
print('-----------------------------')

# 测试所有边是否可以打印，用权值表示
all_edges_aaa = b.iteroutedges("C")
for i in all_edges_aaa:
    print(i)

print('-----------------------------')

# b.show()