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


def get_all_edges_from_graph(graph):
    edges = []
    edges_without_weight = []
    for vertice in graph:
        #         make_set(vertice)  # 初始化所有节点，高度为0，头结点指向自己
        for target in graph[vertice].keys():  # 把所有的边抓出来
            edges.append((vertice, target, graph[vertice][target]))  # 收集了边的权值
            edges_without_weight.append((vertice, target))  # 没有收集了边的权值
    return edges_without_weight


from collections import defaultdict


def num_edges_to_dict(graph):
    all_edges = get_all_edges_from_graph(graph)
    mst_tree_dict = defaultdict(list)  # 初始化一下
    for k, v, in all_edges:
        mst_tree_dict[k].append(v)
    return len(mst_tree_dict.keys())


num_nodes_long = num_edges_to_dict(graph2)
# print('num_nodes: ', num_nodes_long)

all_edges_long = get_all_edges_from_graph(graph2)
# print('all_edges: ', all_edges_long)

# spanning all trees
import copy
from enum import Enum


# define COLOR
class COLOR(Enum):
    WHITE = 1,
    GRAY = 2,
    BLACK = 3


class edge:
    def __init__(self, from_node=0, to_node=0):
        self.from_node = from_node
        self.to_node = to_node


class Vertex:
    def __init__(self, d=0):
        self.d = d
        self.f = 0
        self.parent = -1
        self.color = COLOR.WHITE


WHITE = COLOR.WHITE
GRAY = COLOR.GRAY
BLACK = COLOR.BLACK


# graph
class graph:
    def __init__(self, V=1):
        self.V = V  # the number of the nodes in graph
        # self.nverteces_originally_connected = 0
        self.root_vertex = 0
        self.edge = [[] for i in range(self.V)]
        self.time = 0
        self.vertex = [Vertex() for i in range(V)]

    # debug

    def load_graph(self, graph):
        pass

    def print_vertex(self):
        for i in range(len(self.vertex)):
            print('vertex ', i, 'is:', self.vertex[i].d, self.vertex[i].f, self.vertex[i].parent, self.vertex[i].color)

    def ownsvertex(self, ind):
        if len(self.edge[ind]) > 0:
            return 1
        for i in range(len(self.edge)):
            for j in range(len(self.edge[i])):
                if self.edge[i][j] == ind:
                    return 1
        return 0

    def nonownedge(self, *oneedge):
        def nonownedge1(self, oneedge):
            for i in range(len(self.edge[oneedge.from_node])):
                if self.edge[oneedge.from_node][i] == oneedge.to_node:
                    return 0
            return 1

        def nonownedge2(self, from_node, to_node):
            for i in range(len(self.edge[from_node])):
                if self.edge[from_node][i] == to_node:
                    return 0
            return 1

        if len(oneedge) == 1:
            return nonownedge1(self, *oneedge)
        else:
            return nonownedge2(self, *oneedge)

    def removeedge(self, from_node, to_node):
        if self.nonownedge(edge(from_node, to_node)):
            return 1
        else:
            self.edge[from_node].remove(to_node)

    def addedge(self, from_node, to_node):
        if self.nonownedge(edge(from_node, to_node)) == 1:
            self.edge[from_node].append(to_node)
        else:
            print('edge from ', from_node, 'to ', to_node, 'has been added')

    def graph_print(self):
        print("the graph is:")
        for i in range(len(self.edge)):
            print('vertex ', i, ': ', self.edge[i])

    def DFS_Visit(self, u):
        self.vertex[u].color = GRAY
        self.time = self.time + 1
        self.vertex[u].d = self.time

        for i in range(len(self.edge[u])):
            if self.vertex[self.edge[u][i]].color == WHITE:
                self.vertex[self.edge[u][i]].parent = u
                self.DFS_Visit(self.edge[u][i])

        self.vertex[u].color = BLACK
        self.time = self.time + 1
        self.vertex[u].f = self.time

    def getNconnectedverteces(self):
        Nconnected = 0
        tally = [0 for i in range(self.V)]
        for i in range(self.V):
            if len(self.edge[i]) > 0:
                tally[i] = tally[i] + 1
        for i in range(len(self.edge)):
            for j in range(len(self.edge[i])):
                tally[self.edge[i][j]] = tally[self.edge[i][j]] + 1
        for i in range(len(tally)):
            if tally[i] > 0:
                Nconnected = Nconnected + 1
        return Nconnected


def GROW(V2, T, L, G, F, nspanningtrees):
    #     global V2
    #     global T
    #     global L
    #     global nspanningtrees
    #     global G
    #     global F
    if T.getNconnectedverteces() == V2:
        L = copy.deepcopy(T)
        nspanningtrees = nspanningtrees + 1
        print("---------spanning tree ", nspanningtrees, "----------\n")
        L.graph_print()
        print("----------------------------------\n")
        L.DFS_Visit(L.root_vertex)
    else:
        FF = []
        while True:
            if len(F) > 0:
                e = F.pop(0)
            else:
                print('F is empty')
                return 0
            v = e.to_node
            T.addedge(e.from_node, v)
            Fcopy = []
            Fcopy = copy.deepcopy(F)

            # add edge to F
            for i in range(len(G.edge[v])):
                w = G.edge[v][i]
                if T.ownsvertex(w) != 1:
                    # print('F:', F)
                    F.insert(0, edge(v, w))

            # delete edge from F
            for iw in range(len(G.edge)):
                atemp = T.ownsvertex(iw)
                if T.ownsvertex(iw):
                    jtmp = []
                    for j in range(len(G.edge[iw])):
                        if G.edge[iw][j] == v:
                            jtmp.append(j)
                    if len(jtmp) > 0:
                        # F.remove(edge(iw,v))
                        iFtemp = []
                        for iF in range(len(F)):
                            if F[iF].from_node == iw and F[iF].to_node == v:
                                iFtemp.append(iF)
                        if len(iFtemp) > 0:
                            for df in range(len(iFtemp) - 1, -1, -1):
                                F.pop(iFtemp[df])

            #             GROW()
            GROW(V2, T, L, G, F, nspanningtrees)
            F = copy.deepcopy(Fcopy)
            T.removeedge(e.from_node, e.to_node)
            G.removeedge(e.from_node, e.to_node)
            FF.insert(0, e)

            # bridge test
            b = 1
            for w in range(len(G.edge)):
                tempjj = -1
                for jj in range(len(G.edge[w])):
                    if G.edge[w][jj] == v:
                        tempjj = jj
                if tempjj != -1:
                    if ((L.vertex[v].d < L.vertex[w].d) and (L.vertex[w].d < L.vertex[w].f) and (
                            L.vertex[w].f < L.vertex[v].f)) == 0:
                        b = 0
                        break
            if b == 1:
                break

        while len(FF) > 0:
            e1 = FF.pop(0)
            F.insert(0, e1)
            G.addedge(e1.from_node, e1.to_node)


# 合并函数
def get_all_spanning_tree(num_of_nodes, all_edges, graph):
    V2 = num_of_nodes
    G = graph(num_of_nodes)

    L = graph(num_of_nodes)
    T = graph(num_of_nodes)
    T.root_vertex = 0
    L.root_vertex = 0
    F = []
    nspanningtrees = 0

    for k, v in all_edges:
        G.addedge(k, v)
    G.graph_print()

    for i in range(len(G.edge[G.root_vertex])):
        F.insert(0, edge(G.root_vertex, G.edge[G.root_vertex][i]))
    return GROW(V2, T, L, G, F, nspanningtrees)


num_of_nodes = 5
all_edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 1), (3, 1), (3, 4), (4, 2)]

# num_of_nodes = 64
# all_edges = [(109, 1), (109, 108), (5, 4), (8, 111), (110, 8), (110, 6), (110, 5), (110, 10), (10, 11), (13, 112),
#               (113, 14), (113, 13), (113, 110), (115, 114), (17, 115), (18, 17), (116, 18), (118, 117), (121, 118),
#               (121, 119), (121, 120), (121, 122), (122, 25), (27, 123), (126, 124), (126, 125), (126, 27), (126, 121),
#               (188, 187), (189, 127), (189, 186), (32, 129), (131, 130), (132, 131), (132, 32), (132, 128), (132, 34),
#               (132, 189), (34, 35), (37, 134), (137, 135), (137, 136), (137, 37), (137, 132), (139, 138), (140, 138),
#               (41, 139), (41, 140), (143, 141), (143, 142), (143, 41), (44, 45), (44, 46), (44, 48), (45, 47), (46, 47),
#               (48, 49), (191, 51), (191, 145), (191, 144), (191, 44), (150, 149), (151, 150), (151, 148), (151, 54),
#               (151, 192), (56, 57), (56, 58), (57, 59), (58, 59), (60, 56), (60, 61), (61, 62), (193, 64), (193, 153),
#               (193, 152), (193, 60), (155, 66), (155, 67), (71, 70), (71, 185), (72, 75), (73, 72), (73, 74), (75, 76),
#               (78, 77), (79, 157), (79, 156), (159, 158), (195, 159), (195, 194), (195, 79), (195, 78), (195, 161),
#               (161, 162), (84, 83), (166, 163), (166, 164), (166, 165), (166, 85), (166, 84), (89, 88), (169, 167),
#               (169, 168), (169, 170), (169, 89), (173, 172), (174, 173), (175, 174), (176, 175), (196, 176), (180, 179),
#               (181, 101), (181, 100), (181, 180), (183, 182), (184, 183), (184, 104)]

a = get_all_spanning_tree(num_of_nodes, all_edges, graph)
print(a)
