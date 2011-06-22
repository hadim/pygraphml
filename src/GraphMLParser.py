#-*- coding: utf-8 -*-

from xml.dom import minidom

from Graph import *
from Node import *
from Edge import *

class GraphMLParser:
    """
    """

    def __init__(self):
        """
        """


    def parse(self, fname):
        """
        """

        dom = minidom.parse(open(fname, 'r'))

        root = dom.getElementsByTagName("graphml")[0]
        graph = root.getElementsByTagName("graph")[0]
        name = graph.getAttribute('id')

        g = Graph(name)

        # # Get attributes
        # attributes = []
        # for attr in root.getElementsByTagName("key"):
        #     attributes.append(attr)

        # Get nodes
        for node in graph.getElementsByTagName("node"):
            n = g.addNode(node.getAttribute('id'))

            for attr in node.getElementsByTagName("data"):
                n[attr.getAttribute("key")] = attr.firstChild.data

        # Get edges
        for edge in graph.getElementsByTagName("edge"):
            source = edge.getAttribute('source')
            dest = edge.getAttribute('target')
            e = g.addEdgeByLabel(source, dest)

            for attr in edge.getElementsByTagName("data"):
                e[attr.getAttribute("key")] = attr.firstChild.data

        return g


if __name__ == '__main__':

    parser = GraphMLParser()
    g = parser.parse('test.graphml')

    g.show(True)
    
        
