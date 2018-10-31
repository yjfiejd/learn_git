import yamada
import networkx as nx

example = {13: {112: {'weight': 0}}, 113: {13: {'weight': 0}, 110: {'weight': 0}, 14: {'weight': 0}},
           10: {11: {'weight': 0}},
           110: {10: {'weight': 0}, 8: {'weight': 0}, 6: {'weight': 0}, 5: {'weight': 0}},
           5: {4: {'weight': 0}}, 8: {111: {'weight': 0}}}
# example = {
#     0: {1: {'weight':10}, 2: {'weight':6}, 3: {'weight':5}},
#     1: {0: {'weight':10}, 3: {'weight':15}},
#     2: {0: {'weight':6}, 3: {'weight':4}},
#     3: {0: {'weight':5}, 1: {'weight':15}, 2: {'weight':4}}
# }


graph = nx.Graph(example)

# retrieve all minimum spanning trees
graph_yamada = yamada.Yamada(graph)
all_msts = graph_yamada.spanning_trees()
for i in all_msts:
    print(i.edges())

print(len(all_msts))

# retrieve fixed number of minimum spanning trees
graph_yamada = yamada.Yamada(graph, n_trees=3)
msts = graph_yamada.spanning_trees()
print(len(msts))
