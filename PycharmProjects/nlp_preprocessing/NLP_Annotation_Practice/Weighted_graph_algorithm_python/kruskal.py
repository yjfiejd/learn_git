from queue import PriorityQueue
from NLP_Annotation_Practice.Weighted_graph_algorithm_python.unionfind import UnionFind


class KruskalMST:
    """Kruskal's algorithm for finding a minimum spanning tree.
    Attributes
    ----------
    graph : input undirected graph or multigraph
    mst : graph (MST)
    _uf : disjoint-set data structure, private
    _pq : priority queue, private

    """

    def __init__(self, graph):
        """
        Parameters
        ----------
        graph : undirected weighted graph or multigraph
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.mst = self.graph.__class__(self.graph.v())
        for node in self.graph.iternodes():  # isolated nodes are possible
            self.mst.add_node(node)
        self._uf = UnionFind()
        self._pq = PriorityQueue()

    def run(self):
        """Finding MST."""
        for node in self.graph.iternodes():
            self._uf.create(node)
        for edge in self.graph.iteredges():
            self._pq.put((edge.weight, edge))
        while not self._pq.empty():
            _, edge = self._pq.get()
            if self._uf.find(edge.source) != self._uf.find(edge.target):
                self._uf.union(edge.source, edge.target)
                self.mst.add_edge(edge)

    def to_tree(self):
        """Compatibility with other classes."""
        return self.mst