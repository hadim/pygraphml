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


def test_graph():
    g = create_graph()
    assert len(g.nodes()) == 5
    assert len(g.edges()) == 4


def test_graph_search():
    g = create_graph()
    g.set_root(g.nodes()[0])

    excepted_ids = [0, 2, 3, 4]
    for node, excepted_id in zip(g.BFS(), excepted_ids):
        assert int(node.id) == excepted_id

    excepted_ids = [0, 2, 3, 4]
    for node, excepted_id in zip(g.DFS_prefix(), excepted_ids):
        assert int(node.id) == excepted_id
