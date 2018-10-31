from NLP_Annotation_Practice.NLP_Annotation_Practice import *


class Graph(dict):

    def __init__(self, n=0, directed=False):
        """
        :param n: int,(positive; not used,for compatibility only)
        :param directed: bool值，默认定义directed为False
        """
        self.n = n
        self.directed = directed
        # Structures defining a topological graph.
        self.edge_next = None
        self.edge_prev = None

    def iternodes(self):
        """
        :return:把图中所有的节点拿出来
        """
        nodelist = []
        for key in self.keys():
            nodelist.append(key)
            print(nodelist)
        return nodelist


graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

graph_2 = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}

a = graph
b = graph_2

print("--------------------------------------------------")


# 找到所有的节点
def get_all_nodes(self):
    return self.keys()


# 找到所有的边
def get_all_edges(self):
    for source in get_all_nodes(self):
        t = source
        print("遍历source节点为{}：".format(t))
        for target in self[source]:
            print("self[source]的值是：{}".format(self[source]))
            yield self[source][target]  # 返回一个迭代器


all_edges_a = get_all_edges(b)  # 打印迭代器
all_edges = []
for i in all_edges_a:
    all_edges.append(i)
    print("i的值为：{}, 边的权值为：{}".format(i, all_edges))

print("--------------------------------------------------")


# print(graph_2["B"]["A"])

# 找出由外指向内的
def iterinedges_aaa(self, source):
    """
    15）:return: 返回inedges,图中的, -> 由target指向source
    """
    if self.is_directed():  # 如果是有向图，
        for target in self.iternodes():  # 对于目标节点（它在整个节点列表中的）
            if source in self[target]:  # 先找出所有的self[target] -> 指向的节点，如果source在其中，则返回
                yield self[target][source]


# 得到字典的key
def get_keys(a):
    b = []
    for i in a.keys():
        b.append(i)
    return b


# print(get_keys(a))


def get_keys_dict(a):
    return a.keys()


#
# print(get_keys_dict(a))
# print(a["A"])
# print(b["A"]["B"])


# 把权值都打印出来
def iteroutedges_aa(self, source):
    """Generate the outedges from the graph on demand."""
    weight_list = []
    for target in self[source]:
        weight_list.append(self[source][target])
    return weight_list


# 把相邻节点拿出来
def iteradjacent_aa(self, source):
    """
    :return: 把节点的相邻节点拿出来
    """
    return list(self[source].keys())

# print(iteroutedges_aa(b, "A"))
#
# print(iteradjacent_aa(b, "A"))
# print(iteradjacent_aa(b, "A"))


# # 仅仅把 A, B, C 作为新的字典拿出来。
# list = ["A", "B", "C"]
# list_a = dict()
# for i in list:
#     list_a[i] = graph_2[i]
# print(list_a)
