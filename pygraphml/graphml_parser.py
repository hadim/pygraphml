# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from xml.dom import minidom

from . import Graph


class GraphMLParser:
    """
    """

    def __init__(self):
        """
        """

    def write(self, graph, fname=None):
        """
        """

        doc = minidom.Document()

        root = doc.createElement('graphml')
        doc.appendChild(root)

        # Add attributs
        for a in graph.get_attributs():
            attr_node = doc.createElement('key')
            attr_node.setAttribute('id', a.name)
            attr_node.setAttribute('attr.name', a.name)
            attr_node.setAttribute('attr.type', a.type)
            root.appendChild(attr_node)

        graph_node = doc.createElement('graph')
        graph_node.setAttribute('id', graph.name)
        if graph.directed:
            graph_node.setAttribute('edgedefault', 'directed')
        else:
            graph_node.setAttribute('edgedefault', 'undirected')
        root.appendChild(graph_node)

        # Add nodes
        for n in graph.nodes():

            node = doc.createElement('node')
            node.setAttribute('id', n['label'])
            for a in n.attributes():
                if a != 'label':
                    data = doc.createElement('data')
                    data.setAttribute('key', a)
                    data.appendChild(doc.createTextNode(str(n[a])))
                    node.appendChild(data)
            graph_node.appendChild(node)

        # Add edges
        for e in graph.edges():

            edge = doc.createElement('edge')
            edge.setAttribute('source', e.node1['label'])
            edge.setAttribute('target', e.node2['label'])
            if e.directed() != graph.directed:
                edge.setAttribute('directed', 'true' if e.directed() else 'false')
            for a in e.attributes():
                if e != 'label':
                    data = doc.createElement('data')
                    data.setAttribute('key', a)
                    data.appendChild(doc.createTextNode(e[a]))
                    edge.appendChild(data)
            graph_node.appendChild(edge)

        if fname is not None:
            f = open(fname, 'w')
            f.write(doc.toprettyxml(indent='    '))
        else:
            return doc.toprettyxml(indent='', newl='')

    @staticmethod
    def parse_dom(dom):
        """Parse dom into a Graph.

        :param dom: dom as returned by minidom.parse or minidom.parseString
        :return: A Graph representation
        """
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
            n = g.add_node(id=node.getAttribute('id'))

            for attr in node.getElementsByTagName("data"):
                if attr.firstChild:
                    n[attr.getAttribute("key")] = attr.firstChild.data
                else:
                    n[attr.getAttribute("key")] = ""

        # Get edges
        for edge in graph.getElementsByTagName("edge"):
            source = edge.getAttribute('source')
            dest = edge.getAttribute('target')

            # source/target attributes refer to IDs: http://graphml.graphdrawing.org/xmlns/1.1/graphml-structure.xsd
            e = g.add_edge_by_id(source, dest)

            for attr in edge.getElementsByTagName("data"):
                if attr.firstChild:
                    e[attr.getAttribute("key")] = attr.firstChild.data
                else:
                    e[attr.getAttribute("key")] = ""

        return g

    def parse(self, fname):
        """
        """

        g = None
        with open( fname, 'r') as f:
            dom = minidom.parse(f)
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
                n = g.add_node(id=node.getAttribute('id'))

                for attr in node.getElementsByTagName("data"):
                    if attr.firstChild:
                        n[attr.getAttribute("key")] = attr.firstChild.data
                    else:
                        n[attr.getAttribute("key")] = ""

            # Get edges
            for edge in graph.getElementsByTagName("edge"):
                source = edge.getAttribute('source')
                dest = edge.getAttribute('target')

                # source/target attributes refer to IDs: http://graphml.graphdrawing.org/xmlns/1.1/graphml-structure.xsd
                e = g.add_edge_by_id(source, dest)
                
                # keep the id of the parsed dom
                e.id = edge.getAttribute('id')

                for attr in edge.getElementsByTagName("data"):
                    if attr.firstChild:
                        e[attr.getAttribute("key")] = attr.firstChild.data
                    else:
                        e[attr.getAttribute("key")] = ""

        return g

    def parse_string(self, string):
        """Parse a string into a Graph.

        :param string: String that is to be passed into Grapg
        :return: Graph
        """
        dom = minidom.parseString(string)
        return self.parse_dom(dom)


if __name__ == '__main__':

    parser = GraphMLParser()
    g = parser.parse('test.graphml')

    g.show(True)
