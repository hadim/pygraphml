# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from xml.dom import minidom
import xml.dom

from pygraphml import Graph, Item


class GraphMLParser:
    """
    """

    def __init__(self):
        """
        """

    def write(self, graph: Graph, fname=None):
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

        graph_element = self._create_graph_element(doc, graph)
        root.appendChild(graph_element)

        if fname is not None:
            f = open(fname, 'w')
            f.write(doc.toprettyxml(indent='    '))
        else:
            return doc.toprettyxml(indent='', newl='')

    def _create_graph_element(self, doc, graph: Graph):
        graph_node = doc.createElement('graph')
        if graph.directed:
            graph_node.setAttribute('edgedefault', 'directed')
        else:
            graph_node.setAttribute('edgedefault', 'undirected')

        # Add nodes
        for n in graph.nodes():

            node = doc.createElement('node')
            node.setAttribute('id', n.id)

            for a in n.attributes():
                data = doc.createElement('data')
                data.setAttribute('key', a)
                data.appendChild(doc.createTextNode(str(n[a])))
                node.appendChild(data)

            nested_graph = n.nested_graph()
            if nested_graph is not None:
                graph_element = self._create_graph_element(doc, nested_graph)
                node.appendChild(graph_element)

            graph_node.appendChild(node)

        # Add edges
        for e in graph.edges():

            edge = doc.createElement('edge')
            edge.setAttribute('source', e.node1.id)
            edge.setAttribute('target', e.node2.id)

            if e.directed() != graph.directed:
                edge.setAttribute('directed', 'true' if e.directed() else 'false')

            for a in e.attributes():
                data = doc.createElement('data')
                data.setAttribute('key', a)
                data.appendChild(doc.createTextNode(e[a]))
                edge.appendChild(data)

            nested_graph = e.nested_graph()
            if nested_graph is not None:
                graph_element = self._create_graph_element(doc, nested_graph)
                edge.appendChild(graph_element)

            graph_node.appendChild(edge)

        return graph_node

    def _parse_dom(self, dom):
        """Parse dom into a Graph.

        :param dom: dom as returned by minidom.parse or minidom.parseString
        :return: A Graph representation
        """
        root = dom.getElementsByTagName("graphml")[0]
        graph = root.getElementsByTagName("graph")[0]

        g = self._parse_graph_element(graph)

        return g

    def _parse_graph_element(self, graph) -> Graph:
        g = Graph()
        g.directed = (graph.getAttribute('edgedefault') == "directed")

        # Get nodes
        for child in graph.childNodes:
            if child.nodeType != xml.dom.Node.ELEMENT_NODE:
                continue

            if child.tagName == "node":
                self._parse_node_element(child, g)
            elif child.tagName == "edge":
                self._parse_edge_element(child, g)

        return g

    def _parse_node_element(self, element, graph: Graph):
        n = graph.add_node(id=element.getAttribute('id'))

        for child in element.childNodes:
            if child.nodeType != xml.dom.Node.ELEMENT_NODE:
                continue

            if child.tagName == "data":
                self._parse_data_element(child, n)
            elif child.tagName == "graph":
                nested_g = self._parse_graph_element(child)
                n.set_nested_graph(nested_g)

    def _parse_edge_element(self, element, graph: Graph):
        source = element.getAttribute('source')
        dest = element.getAttribute('target')

        # source/target attributes refer to IDs: http://graphml.graphdrawing.org/xmlns/1.1/graphml-structure.xsd
        e = graph.add_edge_by_id(source, dest)

        if element.hasAttribute("directed"):
            directed = (element.getAttribute('directed') == "true")
            e.set_directed(directed)

        for child in element.childNodes:
            if child.nodeType != xml.dom.Node.ELEMENT_NODE:
                continue

            if child.tagName == "data":
                self._parse_data_element(child, e)
            elif child.tagName == "graph":
                nested_g = self._parse_graph_element(child)
                e.set_nested_graph(nested_g)

    def _parse_data_element(self, element, item: Item):
        if element.tagName == "data":
            if element.firstChild:
                item[element.getAttribute("key")] = element.firstChild.data
            else:
                item[element.getAttribute("key")] = ""

    def parse(self, fname):
        """
        """

        with open(fname, 'r') as f:
            dom = minidom.parse(f)
            return self._parse_dom(dom)

    def parse_string(self, string):
        """Parse a string into a Graph.

        :param string: String that is to be passed into Grapg
        :return: Graph
        """
        dom = minidom.parseString(string)
        return self._parse_dom(dom)


if __name__ == '__main__':

    parser = GraphMLParser()
    g = parser.parse('test.graphml')

    g.show(True)
