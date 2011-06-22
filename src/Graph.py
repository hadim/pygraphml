#-*- coding: utf-8 -*-

from Node import *
from Edge import *

class Graph:
    """
    """

    def __init__(self):
        """
        """

        self.nodes = []
        self.edges = []

    def addNode(self):
        """
        """

        n = Node()
        self.nodes.append(n)

        return n

    def addEdge(self, n1, n2):
        """
        """

        if n1 not in self.nodes:
            raise Test("fff")
        if n2 not in self.nodes:
            raise Test("fff")

        e = Edge(n1, n2)
        self.edges.append(e)

        return e

    def show(self):
        """
        """

        import matplotlib
        matplotlib.use('TKAgg')

        import matplotlib.pyplot as plt
        import networkx as nx

        G = nx.Graph()

        for n in self.nodes:
            G.add_node(n.id)

        for e in self.edges:
            G.add_edge(e.node1.id, e.node2.id)

        nx.draw(G)
        plt.show()
        
