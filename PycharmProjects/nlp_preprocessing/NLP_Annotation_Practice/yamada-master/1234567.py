import yamada
import networkx as nx

example = [{109: {108: {'weight': 0}, 1: {'weight': 0}}},
           {13: {112: {'weight': 0}},
            113: {13: {'weight': 0}, 110: {'weight': 0}, 14: {'weight': 0}},
            10: {11: {'weight': 0}},
            110: {10: {'weight': 0},
                  8: {'weight': 0},
                  6: {'weight': 0},
                  5: {'weight': 0}},
            5: {4: {'weight': 0}},
            8: {111: {'weight': 0}}},
           {18: {17: {'weight': 0}},
            116: {18: {'weight': 0}},
            115: {114: {'weight': 0}},
            17: {115: {'weight': 0}}},
           {27: {123: {'weight': 0}},
            126: {124: {'weight': 0},
                  27: {'weight': 0},
                  121: {'weight': 0},
                  125: {'weight': 0}},
            122: {25: {'weight': 0}},
            121: {122: {'weight': 0},
                  119: {'weight': 0},
                  120: {'weight': 0},
                  118: {'weight': 0}},
            118: {117: {'weight': 0}}},
           {188: {187: {'weight': 0}}},
           {37: {134: {'weight': 0}},
            137: {135: {'weight': 0},
                  37: {'weight': 0},
                  132: {'weight': 0},
                  136: {'weight': 0}},
            34: {35: {'weight': 0}},
            132: {34: {'weight': 0},
                  131: {'weight': 0},
                  32: {'weight': 0},
                  128: {'weight': 0},
                  189: {'weight': 0}},
            189: {127: {'weight': 0}, 186: {'weight': 0}},
            32: {129: {'weight': 0}},
            131: {130: {'weight': 0}}},
           {143: {141: {'weight': 0}, 142: {'weight': 0}, 41: {'weight': 0}},
            139: {138: {'weight': 0}},
            140: {138: {'weight': 0}},
            41: {139: {'weight': 0}, 140: {'weight': 0}}},
           {191: {144: {'weight': 0},
                  44: {'weight': 0},
                  51: {'weight': 0},
                  145: {'weight': 0}},
            45: {47: {'weight': 0}},
            46: {47: {'weight': 0}},
            48: {49: {'weight': 0}},
            44: {45: {'weight': 0}, 46: {'weight': 0}, 48: {'weight': 0}}},
           {151: {54: {'weight': 0},
                  150: {'weight': 0},
                  148: {'weight': 0},
                  192: {'weight': 0}},
            150: {149: {'weight': 0}}},
           {193: {152: {'weight': 0},
                  60: {'weight': 0},
                  64: {'weight': 0},
                  153: {'weight': 0}},
            60: {56: {'weight': 0}, 61: {'weight': 0}},
            57: {59: {'weight': 0}},
            58: {59: {'weight': 0}},
            61: {62: {'weight': 0}},
            56: {57: {'weight': 0}, 58: {'weight': 0}}},
           {155: {67: {'weight': 0}, 66: {'weight': 0}}},
           {71: {70: {'weight': 0}, 185: {'weight': 0}}},
           {73: {74: {'weight': 0}, 72: {'weight': 0}},
            75: {76: {'weight': 0}},
            72: {75: {'weight': 0}}},
           {161: {162: {'weight': 0}},
            195: {161: {'weight': 0},
                  159: {'weight': 0},
                  194: {'weight': 0},
                  79: {'weight': 0},
                  78: {'weight': 0}},
            79: {157: {'weight': 0}, 156: {'weight': 0}},
            78: {77: {'weight': 0}},
            159: {158: {'weight': 0}}},
           {166: {163: {'weight': 0},
                  164: {'weight': 0},
                  165: {'weight': 0},
                  85: {'weight': 0},
                  84: {'weight': 0}},
            84: {83: {'weight': 0}}},
           {169: {167: {'weight': 0},
                  170: {'weight': 0},
                  168: {'weight': 0},
                  89: {'weight': 0}},
            89: {88: {'weight': 0}}},
           {176: {175: {'weight': 0}},
            196: {176: {'weight': 0}},
            173: {172: {'weight': 0}},
            174: {173: {'weight': 0}},
            175: {174: {'weight': 0}}},
           {181: {101: {'weight': 0}, 100: {'weight': 0}, 180: {'weight': 0}},
            180: {179: {'weight': 0}}},
           {184: {104: {'weight': 0}, 183: {'weight': 0}}, 183: {182: {'weight': 0}}}]

all_edges_finded = []

for i in example:
    # print(i)

    graph = nx.Graph(i)

    # retrieve all minimum spanning trees
    graph_yamada = yamada.Yamada(graph)
    all_msts = graph_yamada.spanning_trees()

    list_b = []
    for i in all_msts:
        a = i.edges()
        list_b.append(a)

    all_edges_finded.append(list_b)
    print('--------------\n')



print(len(all_edges_finded))

print('all_edges_finded: ', all_edges_finded)

# normal_list = []
# for i in all_edges_finded:
#     print(i)

print(all_edges_finded[6])
print(len(all_edges_finded[6]))


print(all_edges_finded[1])
print(len(all_edges_finded[1]))



