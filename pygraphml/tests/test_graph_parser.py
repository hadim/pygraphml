import tempfile

from pygraphml import GraphMLParser
from pygraphml import Graph
from pygraphml import Item


def create_graph():
    Item.ID = 0
    g = Graph()

    n1 = g.add_node("A")
    n2 = g.add_node("B")
    n3 = g.add_node("C")
    n4 = g.add_node("D")
    n5 = g.add_node("E")

    g.add_edge(n1, n3)
    g.add_edge(n2, n3)
    g.add_edge(n3, n4)
    g.add_edge(n3, n5)
    return g


def test_graph_io():
    g = create_graph()

    fname = tempfile.mktemp()
    parser = GraphMLParser()
    parser.write(g, fname)

    with open(fname) as f:
        print(f.read())

    parser = GraphMLParser()
    g = parser.parse(fname)

    assert len(g.nodes()) == 5
    assert len(g.edges()) == 4
