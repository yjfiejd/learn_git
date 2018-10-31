

graph = {
    0: {1},
    1: {0, 2, 3},
    2: {1, 3},
    3: {1, 2, 4, 5},
    4: {3, 5},
    5: {3, 4, 6},
    6: {5}
}

graph1 = {
    0: {1: 10, 2: 6, 3: 5},
    1: {0: 10, 3: 15},
    2: {0: 6, 3: 4},
    3: {0: 5, 1: 15, 2: 4}
}


def get_all_edges(graph):
    edges = []
    for i in graph:
        for j in graph[i]:
            edges.append((i, j))
    return edges

all_edges = get_all_edges(graph1)


print(len(all_edges))
print(all_edges)