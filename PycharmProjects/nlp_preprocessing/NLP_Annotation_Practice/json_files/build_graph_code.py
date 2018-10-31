import json

def build_graph(annotation, block_category=[]):
    reverse_set = {124}
    block_id = []
    graph_in = dict()
    graph_out = dict()
    graph_undirected = dict()
    for node in annotation['labels']:
        graph_in[node['id']] = {'type': node['category']}
        graph_out[node['id']] = {'type': node['category']}
        graph_undirected[node['id']] = {'type': node['category']}
        # graph_in[node['id']] = {}
        # graph_out[node['id']] = {}
        # graph_undirected[node['id']] = {}

        if node['category'] in block_category:
            block_id.append(node['id'])

    relations = annotation['relations']

    for item in relations:
        if item['src'] in block_id or item['dst'] in block_id:
            continue

        # if item['category'] in reverse_set:
        #     src = item['dst']
        #     dst = item['src']
        #     category = 86
        # else:

        dst = item['dst']
        src = item['src']
        category = item['category']

        try:
            graph_out[src][dst] = category
            # print(graph_in)
        except:
            pass
            # print('error:', annotation['id'])
        try:
            graph_in[dst][src] = category
        except:
            pass
            # print('error:', annotation['id'])

        try:
            graph_undirected[src][dst] = category
        except:
            pass
            # print('error:', annotation['id'])

        try:
            graph_undirected[dst][src] = category
        except:
            pass
            # print('error:', annotation['id'])

    # for node in graph_in


    for node in graph_in:
        graph_in[node].__delitem__('type')
    for node in graph_out:
        graph_out[node].__delitem__('type')
    for node in graph_undirected:
        graph_undirected[node].__delitem__('type')

    # return graph_in, graph_out, graph_undirected
    return graph_in



def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


def graph_traversal(graph):
    trees = []

    node_set = set(graph.keys())

    while node_set:
        start = node_set.pop()
        a = dfs(graph, start)
        trees.append(a)
        node_set -= a

    return trees


if __name__ == "__main__":

    with open("annotation37529-37538.json", 'r') as f:
        temp = json.loads(f.read())
        print(build_graph(temp[0]))