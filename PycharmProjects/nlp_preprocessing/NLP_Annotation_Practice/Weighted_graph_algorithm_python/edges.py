class Edge:
    """
    定义有向边:
    属性：source, target, weight
    """

    def __init__(self, source, target, weight=1):
        """
        :param source: 起点
        :param target: 终点
        :param weight: 权重
        """
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        """
        :return: 重构字符串的表达形式
        """
        if self.weight == 1:
            return "{} ({}) ".format(
                # self.__class__.__name__,
                repr(self.source),
                repr(self.target)
            )
        else:
            return "{} ({}, {})".format(
                # self.__class__.__name__,
                repr(self.source),
                repr(self.target),
                repr(self.weight)
            )

    def __cmp__(self, other):
        """
        :param other:
        :return: 对比边的权重
        """
        if self.weight > other.weight:
            return 1
        if self.weight < other.weight:
            return -1

        if self.source > other.source:
            return 1
        if self.source < other.source:
            return -1

        if self.target > other.target:
            return 1
        if self.target < other.target:
            return -1
        return 0




class UndirectedEdge(Edge):
    """
    the class defining and undirected edge. 初始化无向图的边，小的在前，大的再后
    """

    def __init__(self, source, target, weight=1):

        if source > target:
            self.source = target
            self.target = source

        else:
            self.source = source
            self.target = target
        self.weight = weight

    # __invert__(self) 实现 ~ 符号的特性。为了说明这个特性。你可以查看 Wikipedia中的这篇文章 <http://en.wikipedia.org/wiki/Bitwise_operation#NOT>_
    def __invert__(self):
        """
        the edge direction is not defined.
        """
        return self
