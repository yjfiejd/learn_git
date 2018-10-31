
import unittest
from NLP_Annotation_Practice.Weighted_graph_algorithm_python.edges import Edge
from NLP_Annotation_Practice.Weighted_graph_algorithm_python.graphs import Graph
from NLP_Annotation_Practice.Weighted_graph_algorithm_python.kruskal import KruskalMST



class TestKruskal(unittest.TestCase):

    def setUp(self):
        # The graph (unique weights) from
        # http://en.wikipedia.org/wiki/Boruvka's_algorithm
        self.N = 7           # number of nodes
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1, 7), Edge(1, 2, 11), Edge(0, 3, 4),
            Edge(3, 1, 9), Edge(4, 1, 10), Edge(2, 4, 5), Edge(3, 4, 15),
            Edge(3, 5, 6), Edge(5, 4, 12), Edge(5, 6, 13), Edge(4, 6, 8)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_kruskal(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = KruskalMST(self.G)
        algorithm.run()
        self.assertEqual(algorithm.mst.v(), self.N)
        self.assertEqual(algorithm.mst.e(), self.N-1)
        mst_weight_expected = 40
        mst_weight = sum(edge.weight for edge in algorithm.mst.iteredges())
        self.assertEqual(mst_weight, mst_weight_expected)
        mst_edges_expected = [
            Edge(0, 1, 7), Edge(0, 3, 4), Edge(2, 4, 5), Edge(1, 4, 10),
            Edge(4, 6, 8), Edge(3, 5, 6)]
        for edge in mst_edges_expected:
            self.assertTrue(algorithm.mst.has_edge(edge))


if __name__ == "__main__":

    unittest.main()