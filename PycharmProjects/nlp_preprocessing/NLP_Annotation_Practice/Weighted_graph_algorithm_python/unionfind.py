
class UnionFind:
    '''
    Disjoint-set data structure
    '''

    def __init__(self):
        """
        初始化，定义parent字典，高度字典
        """
        self.parent = dict()
        self.rank = dict()

    def create(self, x):
        """"
        :param x: 输入节点x
        :return: 初始化定义头结点指向自己，初始化该节点所在集合高度为rang=0
        """
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x):
        """
        :param x: 输入节点x，
        :return: 找到它所在的集合头结点 (递归)
        """
        if x != self.parent:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        :param x: 输入节点x
        :param y: 输入节点y
        :return: 将x所在头结点（集合）与y所在头结点（集合）合并
        """
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return

        if self.rank[rootx] < self.rank[rooty]:
            self.parent[rootx] = rooty
        elif self.rank[rootx] > self.rank[rooty]:
            self.parent[rooty] = rootx
        else:
            self.rank[rooty] = self.rank[rooty] + 1

