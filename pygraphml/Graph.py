#-*- coding: utf-8 -*-

from Node import *
from Edge import *

from collections import deque

class Graph:
    """
    Main class which represent a Graph

    :param name: name of the graph
    """

    def __init__(self, name = ""):
        """
        """

        self.name = name

        self._nodes = []
        self._edges = []
        self._root = None
        self.directed = True

        self.i = 0

    def DFS_prefix(self, root = None):
        """
        Depth-first search.

        .. seealso::
           `Wikipedia DFS descritpion <http://en.wikipedia.org/wiki/Depth-first_search>`_

        :param root: first to start the search
        :return: list of nodes
        """

        if not root:
            root = self._root

        return self._DFS_prefix(root)

    def _DFS_prefix(self, n, parent = None):
        """	
        """

        nodes = [n]
        n['depth'] = self.i

        for c in n.children():
            nodes += self._DFS_prefix(c, n)
            self.i += 1

        return nodes

    def BFS(self, root = None):
        """
        Breadth-first search.

        .. seealso::
           `Wikipedia BFS descritpion <http://en.wikipedia.org/wiki/Breadth-first_search>`_

        :param root: first to start the search
        :return: list of nodes

        
        """

        if not root:
            root = self.root()

        queue = deque()
        queue.append(self.root())

        nodes = []

        self.depth = 0
        
        while len(queue) > 0:
            x = queue.popleft()
            nodes.append(x)
            
            for child in x.children():
                queue.append(child)

        return nodes
        
    def get_depth(self, node):
        """
        """

        depth = 0
        while node.parent() and node != self.root():
            node = node.parent()[0]
            depth += 1

        return depth

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
            if n['label'] == label2:
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
            if n[attribute] in value:
                self.set_root(n)
                return n

    def get_attributs(self):
        """
        """

        attr = []
        attr_obj = []
        for n in self.nodes():
            for a in n.attr:
                if a not in attr:
                    attr.append(a)
                    attr_obj.append(n.attr[a])

        for e in self.edges():
            for a in e.attr:
                if a not in attr:
                    attr.append(a)
                    attr_obj.append(e.attr[a])

        return attr_obj
            

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
        
