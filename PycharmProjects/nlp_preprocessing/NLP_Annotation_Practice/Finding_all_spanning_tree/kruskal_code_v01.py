from collections import defaultdict

# from NLP_Annotation_Practice.kruskal_code.DFS_for_all_nodes import DFS_all_nodes, DFS

graph1 = {
    0: {1: 10, 2: 6, 3: 5},
    1: {0: 10, 3: 15},
    2: {0: 6, 3: 4},
    3: {0: 5, 1: 15, 2: 4}
}

graph3 = {
    "A": {"B": 7, "D": 5},
    "B": {"A": 7, "C": 8, "D": 9, "E": 7},
    "C": {"B": 8, "E": 5},
    "D": {"A": 5, "B": 9, "E": 15, "F": 6},
    "E": {"B": 7, "C": 5, "D": 15, "F": 8, "G": 9},
    "F": {"D": 6, "E": 8, "G": 11},
    "G": {"E": 9, "F": 11}
}

graph2 = {106: {},
          1: {},
          108: {},
          109: {1: 135, 108: 134},
          107: {},
          4: {},
          5: {4: 135},
          6: {},
          111: {},
          8: {111: 138},
          110: {8: 134, 6: 134, 5: 135, 10: 124},
          10: {11: 121},
          11: {},
          112: {},
          13: {112: 31},
          14: {},
          113: {14: 134, 13: 86, 110: 99},
          114: {},
          115: {114: 135},
          17: {115: 135},
          18: {17: 86},
          116: {18: 86},
          117: {},
          118: {117: 135},
          119: {},
          120: {},
          121: {118: 135, 119: 134, 120: 134, 122: 124},
          122: {25: 121},
          25: {},
          123: {},
          27: {123: 31},
          124: {},
          125: {},
          126: {124: 86, 125: 134, 27: 86, 121: 99},
          127: {},
          190: {},
          186: {},
          187: {},
          188: {187: 127},
          189: {127: 135, 186: 135},
          128: {},
          129: {},
          32: {129: 138},
          130: {},
          131: {130: 139},
          132: {131: 134, 32: 134, 128: 134, 34: 124, 189: 135},
          34: {35: 121},
          35: {},
          134: {},
          37: {134: 31},
          135: {},
          136: {},
          137: {135: 86, 136: 134, 37: 86, 132: 99},
          138: {},
          139: {138: 135},
          140: {138: 135},
          41: {139: 135, 140: 135},
          141: {},
          142: {},
          143: {141: 86, 142: 134, 41: 135},
          44: {45: 124, 46: 124, 48: 124},
          45: {47: 121},
          46: {47: 121},
          47: {},
          48: {49: 121},
          49: {},
          144: {},
          145: {},
          51: {},
          191: {51: 134, 145: 134, 144: 86, 44: 99},
          192: {},
          54: {},
          148: {},
          149: {},
          150: {149: 139},
          151: {150: 134, 148: 134, 54: 86, 192: 135},
          56: {57: 124, 58: 124},
          57: {59: 121},
          58: {59: 121},
          59: {},
          60: {56: 99, 61: 124},
          61: {62: 121},
          62: {},
          152: {},
          153: {},
          64: {},
          193: {64: 134, 153: 134, 152: 86, 60: 99},
          66: {},
          67: {},
          155: {66: 135, 67: 86},
          185: {},
          70: {},
          71: {70: 86, 185: 135},
          72: {75: 124},
          73: {72: 135, 74: 121},
          74: {},
          75: {76: 121},
          76: {},
          77: {},
          78: {77: 135},
          156: {},
          157: {},
          79: {157: 134, 156: 138},
          158: {},
          159: {158: 139},
          194: {},
          195: {159: 134, 194: 134, 79: 134, 78: 135, 161: 124},
          161: {162: 121},
          162: {},
          83: {},
          84: {83: 135},
          85: {},
          163: {},
          164: {},
          165: {},
          166: {163: 86, 164: 134, 165: 134, 85: 135, 84: 135},
          88: {},
          89: {88: 135},
          167: {},
          168: {},
          169: {167: 86, 168: 134, 170: 121, 89: 135},
          170: {},
          171: {},
          172: {},
          173: {172: 135},
          174: {173: 135},
          175: {174: 135},
          176: {175: 86},
          196: {176: 86},
          179: {},
          180: {179: 135},
          100: {},
          101: {},
          181: {101: 134, 100: 135, 180: 135},
          182: {},
          183: {182: 135},
          104: {},
          184: {183: 135, 104: 134}
          }

parent = dict()
rank = dict()  # 各点的初始等级均为0,如果被做为连接的的末端，则增加1


# 初始化
def make_set(vertice):
    parent[vertice] = vertice  # 字典添加值, 节点的父节点设置为自己
    rank[vertice] = 0  # 节点的高度设置为0


# 找父节点
def find(vertice):
    if parent[vertice] != vertice:  # 如果没有找到头结点
        parent[vertice] = find(parent[vertice])  # 指针指向原父节点，继续往上找
    return parent[vertice]  # 返回父节点


# 合并两个节点,所在的集合
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


# 查找图中所有相连的边
def find_all_edges(graph):
    all_edges = []
    for vertice in graph:
        for target in graph[vertice].keys():  # 把所有的边抓出来
            all_edges.append((vertice, target))
    return all_edges


# 查找由图 -> 生成树中缺失的 边
def find_diff(A, B):
    more_edges = []
    for i in A:
        if i not in B:
            more_edges.append(i)
    return more_edges


# https://blog.csdn.net/u011475210/article/details/77769245def kruskal(graph):
# Python3：sorted()函数及列表中的sort()函数
def kruskal(graph):
    edges = []
    edges_without_weight = []
    for vertice in graph:
        make_set(vertice)  # 初始化所有节点，高度为0，头结点指向自己
        for target in graph[vertice].keys():  # 把所有的边抓出来
            edges.append((vertice, target, graph[vertice][target]))  # 收集了边的权值
            edges_without_weight.append((vertice, target))  # 没有收集了边的权值

    minimum_spanning_tree = set()  # 初始化，最小生成树的set
    # minimum_spanning_tree_dict = {} #尝试保存为dict格式，方便后续DFS

    #  利用sorted 对边的权值进行排序
    # print(edges)
    edges = sorted(edges, key=lambda edges: edges[2])
    edges_len = len(edges)
    print('\n')
    print("图中的边一共找到{}条边，排序后结果为：\n{}".format(edges_len, edges))
    print("图中的边一共找到{}条边（不含权值）结果为：\n{}".format(edges_len, edges_without_weight))

    for edge in edges:
        vertice1, vertice2, weight = edge  # 对边里面的变量命名
        if find(vertice1) != find(vertice2):  # 两个节点所在集合，不在一起
            union(vertice1, vertice2)  # 合并
            minimum_spanning_tree.add((vertice1, vertice2))  # 在set最小生成树中插入边
    return minimum_spanning_tree


# ********************************
# mst_tree = kruskal(graph1)
mst_tree = kruskal(graph2)  # 找出了所有连通最小生成树，dict的形式
# Mst_tree = kruskal(graph3)
mst_tree_len = len(mst_tree)
# ********************************
print('\n')
print("最小生成树中一共有{}条边，结果为：\n{}".format(mst_tree_len, mst_tree))

all_edges = find_all_edges(graph2)
diff_edges = find_diff(all_edges, mst_tree)
print('\n')
print("原图中的边比生成树多出的边是：{}".format(diff_edges))


# 把dict的图的形式变为字典形式
def mst_tree_to_dict(self):
    """
    :param self: 传入最小生成树的结果，（是用边的形式表达生成的树）
    :return: 返回二维字典形式（每个节点与谁相连） -> 后续用DFS全部遍历
    """
    mst_tree_dict = defaultdict(list)  # 初始化一下
    for k, v, in self:
        mst_tree_dict[k].append(v)
    return mst_tree_dict


mst_tree_dict = mst_tree_to_dict(mst_tree)
print('\n')
print("把最小生成树结果转为字典格式为：{}".format(mst_tree_dict))


# 得到每个节点后续的路径 ->  后续需要找到缺失的边
def DFS(graph, s):
    """
    :param graph: 传入图
    :param s: 传入开始的头结点
    :return: 返回这个图的深度遍历序列list，其实就是子树所有的节点
    """
    stack = []
    seen = set()
    stack.append(s)
    seen.add(s)
    node_seq = []

    while (len(stack) > 0):
        vertex = stack.pop()  # 弹出最后一个元素
        node_seq.append(vertex)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        # print(vertex)
    # print(seen)
    return node_seq


# 获取每个子图,的路径
def all_connected_tree(self):
    """
    :param self: 输入一个二维图字典
    :return: 找到每一个节点的，DFS子图节点
    """
    all_connected_tree = []
    all_nodes = []
    for node in self:  # 找到所有的节点all_edges2
        all_nodes.append(node)
    for node in all_nodes:  # 对每个节点DFS路径
        single_node_path = DFS(self, node)  # 把字典传入，节点传入
        all_connected_tree.append(single_node_path)
    return all_connected_tree


sub_tree = all_connected_tree(mst_tree_dict)

print('\n')
print("该图中可以分解为{}个子树，分别是：\n {}".format(len(sub_tree), sub_tree))
