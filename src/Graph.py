#-*- coding: utf-8 -*-

from Node import *
from Edge import *

class Graph:
    """
    """

    def __init__(self, name = ""):
        """
        """

        self.name = name

        self.nodes = []
        self.edges = []

    def addNode(self, label = ""):
        """
        """

        n = Node()
        n['label'] = label
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

    def addEdgeByLabel(self, label1, label2):
        """
        """

        n1 = None
        n2 = None

        for n in self.nodes:
            if n['label'] == label1:
                n1 = n
            elif n['label'] == label2:
                n2 = n

        if n1 and n2:
            return self.addEdge(n1, n2)
        else:
            return

    def show(self, show_label = False):
        """
        """

        import matplotlib
        matplotlib.use('TKAgg')

        import matplotlib.pyplot as plt
        import networkx as nx

        G = nx.Graph()

        for n in self.nodes:
            if show_label:
                n_label = n['label']
            else:
                n_label = n.id
            G.add_node(n_label)

        for e in self.edges:
            if show_label:
                n1_label = e.node1['label']
                n2_label = e.node2['label']
            else:
                n1_label = e.node1.id
                n2_label = e.node2.id
            G.add_edge(n1_label, n2_label)

        nx.draw(G)
        plt.show()
        
