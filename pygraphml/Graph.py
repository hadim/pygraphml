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

        self._nodes = []
        self._edges = []
        self._root = None
        self.directed = True

    def DFS_prefix(self, root = None):
        """
        """

        if not root:
            root = self._root

        return self._DFS_prefix(root)

    def _DFS_prefix(self, n, parent = None):
        """	
        """

        nodes = [n]
        for c in n.children():
            nodes += self._DFS_prefix(c, n)

        return nodes

    def nodes(self, ):
        """
        """

        return self._nodes

    def edges(self, ):
        """
        """

        return self._edges

    def children(self, node):
        """
        """

        return node.children()

    def add_node(self, label = ""):
        """
        """

        n = Node()
        n['label'] = label
        self._nodes.append(n)

        return n

    def add_edge(self, n1, n2, directed = False):
        """
        """

        if n1 not in self._nodes:
            raise Test("fff")
        if n2 not in self._nodes:
            raise Test("fff")

        e = Edge(n1, n2, directed)
        self._edges.append(e)

        return e

    def add_edge_by_label(self, label1, label2):
        """
        """

        n1 = None
        n2 = None

        for n in self._nodes:
            if n['label'] == label1:
                n1 = n
            elif n['label'] == label2:
                n2 = n

        if n1 and n2:
            return self.add_edge(n1, n2)
        else:
            return

    def set_root(self, node):
        """
        """

        self._root = node

    def root(self):
        """
        """

        return self._root

    def set_root_by_attribute(self, value, attribute = 'label'):
        """
        """

        for n in self.nodes():
            if n[attribute] == value:
                self.set_root(n)
                return n

    def show(self, show_label = False):
        """
        """

        import matplotlib
        matplotlib.use('GTKAgg')

        import matplotlib.pyplot as plt
        import networkx as nx

        G = nx.Graph()

        for n in self._nodes:
            if show_label:
                n_label = n['label']
            else:
                n_label = n.id
            G.add_node(n_label)

        for e in self._edges:
            if show_label:
                n1_label = e.node1['label']
                n2_label = e.node2['label']
            else:
                n1_label = e.node1.id
                n2_label = e.node2.id
            G.add_edge(n1_label, n2_label)

        nx.draw(G)
        plt.show()
        
