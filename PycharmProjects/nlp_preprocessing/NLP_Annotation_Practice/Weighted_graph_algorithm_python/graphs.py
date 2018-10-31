from NLP_Annotation_Practice.Weighted_graph_algorithm_python.edges import Edge


class Graph(dict):
    """
    The class defining a graph.
    Nodes can be numbers, strings, or any hashable objects.
    We would like to compare nodes.

    An exemplary graph structure:
    {"A": {"B": Edge("A", "B", 1), "C": Edge("A", "C", 2)},
    "B": {"C": Edge("B", "C", 3), "D": Edge("B", "D", 4)},
    "C": {"D": Edge("C", "D", 5)},
    "D": {"C": Edge("D", "C", 6)},
    "E": {"C": Edge("E", "C", 7)},
    "F": {}}
    """

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

    def is_directed(self):
        """
        1）:return: 是否是有向图？
        """
        return self.directed

    def v(self):
        """
        2）:return: 返回节点个数
        """
        return len(self)

    def e(self):
        """
        3）:return: 返回边的个数  O(V)
        """
        edges = sum(len(self[node]) for node in self)  # 找到每个节点连接的边的数量
        return edges if self.is_directed() else edges / 2  # 这个是图完全联通的情况下计算方式，没有计算孤立的点

    def f(self):
        """
        4）:return: 连同区域考虑一下
        """
        if not self.edge_next or not self.edge_prev:
            raise ValueError("run plannarity test first")
        return self.e() + 2 - self.n

    def add_node(self, node):
        """
        5）在图中添加节点
        """
        if node not in self:
            self[node] = dict()

    def has_node(self, node):
        """
        6）判断节点是否在图中
        """
        return node in self

    def del_node(self, node):
        """
        7）删除图中的节点，同时删除它的边
        """
        for edge in list(self.iterinedges(node)):
            self.del_edge(edge)
        if self.is_directed():
            for edge in list(self.iteroutedges(node)):
                self.del_edge(edge)
        del self[node]

    def add_edge(self, edge):
        """
        8）把边加入到图当中（会把缺失的节点补上），不允许出现环 & 平行边
        """
        if edge.source == edge.target:
            raise ValueError("Loops are forbidden")
        self.add_node(edge.source)
        self.add_node(edge.target)
        if edge.target not in self[edge.source]:
            self[edge.source][edge.target] = edge
        else:
            # 意思是外来一条边，它指向的target，在图中已经有其他节点指向了，不允许出现平行边
            raise ValueError("Parallel edges are forbidden")

    def del_edge(self, edge):
        """
        9）把图中的一条边删除
        """
        del self[edge.source][edge.target]
        if not self.is_directed():  # not与逻辑判断句if连用，代表not后面的表达式为False的时候，执行冒号后面的语句
            del self[edge.target][edge.source]

    def has_edge(self, edge):
        """
        10）判断这条边是否在图中（只检查source,target,不检查weight）
        """
        return edge.source in self and edge.target in self[edge.source]

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
        # 方法一：返回list格式
        # key_list = []
        # for i in self.keys():
        #     key_list.append(i)
        # return key_list
        return self.keys()  # 方法二：强制转换为list格式，list(self.keys())

    def iteradjacent(self, source):
        """
        13）:return: 把节点的相邻节点拿出来
        """
        return self[source].keys()

    def iteroutedges(self, source):
        """
        14）:return: 【权值返回】返回outedges,图中的 -> 由source指向target 的权值 -> 找到那些由source指出去的权值（类别）
        """
        for target in self[source]:
            yield self[source][target]

    def iterinedges(self, source):
        """
        15）:return: 【权值返回】返回inedges,图中的, -> 由target指向source 的权值 -> 找到那些指向这个source的权值（类别）
        """
        if self.is_directed():  # 如果是有向图，
            for target in self.iternodes():  # 对于目标节点（它在整个节点列表中的）
                if source in self[target]:  # 先找出所有的self[target] -> 指向的节点，如果source在其中，则返回
                    yield self[target][source]

    def iteredges(self):
        """
        16) :return: 把图中所有的边都拿出来, 这里忽略了有向图无向图的变化
        """
        for source in self.iternodes():
            for target in self[source]:
                yield self[source][target]

    def show(self):
        """
        17) :return: 把图打印出来 ??????
        """
        for source in self.iternodes():
            print("{} :".format(source))
            for edge in self.iteroutedges(source):
                if edge.weight == 1:
                    print(edge.target)
                else:
                    print("{} ({})".format(edge.target, edge.weight))

    def complement(self):
        """
        18) :return: 2个图，如果图1中没有包含图2的边，那么把图2的边加入图1，返回新图
        """
        new_graph = Graph(n=self.n, directed=self.directed)
        for node in self.iternodes():
            new_graph.add_node(node)
        for source in self.iternodes():
            for target in self.iternodes():
                if source != target:  # 没有环
                    edge = Edge(source, target)
                    if not self.has_edge(edge) and not new_graph.has_edge(edge):
                        new_graph.add_edge(edge)
        return new_graph

    def subgraph(self, nodes):
        """
        19) :param nodes: 给定一个节点集合
        :return: 返回它们的子图
        """
        node_set = set(nodes)
        # any(iterable) 只有里面全为0,全为False才返回False，否则返回True
        # 下面这行意思是：只要有一个node不在set(nodes)中，则判定node不在图中
        if any(not self.has_node(node) for node in node_set):
            raise ValueError("nodes not from the graph")
        new_graph = Graph(n=len(node_set), directed=self.directed)
        for node in node_set:  # 添加节点
            new_graph.add_node(node)
        for edge in self.iteredges():  # 添加边
            if (edge.source in node_set) and (edge.target in node_set):
                new_graph.add_edge(edge)
        return new_graph

    def __eq__(self, other):
        """
        20) :param other: 其他的图, 传入
        :return: 判断这两个图是否相同
        """
        if self.is_directed() is not other.is_directed():
            return False
        if self.v() != other.v():
            return False
        for node in self.iternodes():
            if not other.has_node(node):
                return False
        if self.e() != other.e():
            return False
        for edge in self.iteredges():
            # 当 other 中不包含 self中的edge时候，返回False
            if not other.has_edge(edge):  # if not 后面表达式为Fasle时候执行冒号语句
                return False
            # 当 self边的权重不等于 other边中的权重，返回False
            if edge.weight != other.weight(edge):
                return False
        return True

    def __ne__(self, other):
        """
       21) :param other: 输入其他图
        :return: 判断不等于，若不等于返回True
        """
        return not self == other

    def add_graph(self, other):
        """
        22) :param other: 把别的图添加在原图中
        :return: 修改了原图中的节点与边
        """
        if self.is_directed() is not other.is_directed():
            raise ValueError("directed vs undirected")
        for node in other.iternodes():
            self.add_node(node)
        for edge in other.itereges():
            self.add_edge(edge)

    def save(self, file_name, name="Graph"):
        """
        :param file_name:
        :param name:
        :return:  返回邻接表的形式表达图
        """
        afile = open(file_name, "w")
        afile.write("# NAME = {} \n".format(name))
        afile.write("# DIRECTED = {} \n".format(self.is_directed()))
        afile.write("# V = {} \n".format(self.v()))
        afile.write("# E = {} \n".format(self.e()))

        for edge in self.iternodes():
            if edge.weight == 1:
                afile.write("{} {} \n".format(edge.source, edge.target))
            else:
                afile.write("{} {} {} \n".format(edge.source, edge.target, edge.weight))
        afile.close()
