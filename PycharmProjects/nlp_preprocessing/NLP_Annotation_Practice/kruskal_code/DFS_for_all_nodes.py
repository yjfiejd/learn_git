
# 建立图-字典
# graph = {
#     "A": {"B": 5, "C": 1},
#     "B": {"A": 5, "C": 2, "D": 1},
#     "C": {"A": 1, "B": 2, "D": 4, "E": 8},
#     "D": {"B": 1, "C": 4, "E": 3, "F": 6},
#     "E": {"C": 8, "D": 3},
#     "F": {"D": 6}
# }


graph = {106: {},
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


# 1）返回图中节点的个数
def vertex_num(graph_in):
    return list(graph_in.keys())


print("图的节点个数是：{} 个".format(len(vertex_num(graph))))
print("图中的节点分别是:{}".format(vertex_num(graph)))


# 2）遍历图中的节点
def iternodes_aa(graph_in):
    return graph_in.keys()


# 3) 遍历图中的边
def iteredges_aa(graph_in):
    edges_list = []
    for source in graph_in:
        for target in graph_in[source]:
            edges_list.append((source, target))
    return edges_list


c = iteredges_aa(graph)

print("图中已经存在的边为：{}".format(c))

print("-----")


# 4）输入一个节点，找出和它相连的所有路径
def DFS(graph, s):
    stack = []
    node_seq = []
    seen = set()
    stack.append(s)
    seen.add(s)

    while (len(stack) > 0):
        vertex = stack.pop()
        node_seq.append(vertex)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
    #         print(vertex)
    return node_seq


# 5）深度遍历所有的节点，找到他们的路径
def DFS_all_nodes(graph):
    total_seq = []
    for node in graph:
        total_seq.append(DFS(graph, node))
    return total_seq


all_nodes_path = DFS_all_nodes(graph)
print("每个节点所能到达的路径，list第一个数字为头结点：\n {}".format(DFS_all_nodes(graph)))
# print(DFS_all_nodes(graph))
print("\n")

# 6） 把真正孤立的节点找出来

total_path = all_nodes_path


def find_isolate_node(total_path):
    isolate_node = []
    larger_node = []
    for node_path in total_path:
        if len(node_path) == 1:
            isolate_node.append(node_path)
        else:
            larger_node.append(node_path)
    return isolate_node, larger_node


single_larger_node = find_isolate_node(all_nodes_path)
a_single = single_larger_node[0]
a_larger = single_larger_node[1]


# 为了获取真正的孤立的节点，有些节点为叶子节点需要去掉
def find_real_isolate_node(single_node, larger_node):
    new_single_path = single_node  # 新建一个列表，单个元素的
    new_total_path = []  # 新建一个空的列表，把larger二维数组，变成一维
    for j in larger_node:
        for h in j:
            new_total_path.append(h)  # 获得了larger的一维数组，单个节点在这出现过，就删除，

    for i in single_node:
        if i[0] in new_total_path:
            new_single_path.remove(i)
    return new_single_path


real_isolate_node = find_real_isolate_node(a_single, a_larger)
len_real_isolate_node = len(real_isolate_node)

print("真正的孤立的节点集合如下(单个节点表示没有任何箭头连出或连入)，共计{}个：\n {}".format(len_real_isolate_node, real_isolate_node))
print("\n")


# 7）未处理子图路径如下：

def find_real_connected_node(real_isolate_node, total_path):
    for i in real_isolate_node:
        if i in total_path:
            total_path.remove(i)
    return total_path


real_connected_node = find_real_connected_node(real_isolate_node, total_path)
len_real_connected_node = len(real_connected_node)
print("真正连接的子树如下（单个节点为叶子节点），共计{}个子图：\n {}".format(len_real_connected_node, real_connected_node))
