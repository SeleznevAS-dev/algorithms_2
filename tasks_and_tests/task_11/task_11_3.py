from .task_11 import SimpleGraph


def test_breadth_first_search():
    simple_graph = SimpleGraph(5)

    simple_graph.AddVertex(1)
    simple_graph.AddVertex(2)
    simple_graph.AddVertex(3)
    simple_graph.AddVertex(4)
    simple_graph.AddVertex(5)
    simple_graph.AddEdge(0, 1)
    simple_graph.AddEdge(0, 2)
    simple_graph.AddEdge(0, 3)
    simple_graph.AddEdge(1, 3)
    simple_graph.AddEdge(1, 4)
    simple_graph.AddEdge(2, 3)
    simple_graph.AddEdge(3, 3)
    simple_graph.AddEdge(3, 4)

    result = simple_graph.BreadthFirstSearch(0, 4)
    assert result == [
        simple_graph.vertex[0],
        simple_graph.vertex[1],
        simple_graph.vertex[4],
    ]

    simple_graph.RemoveEdge(1, 4)
    result = simple_graph.BreadthFirstSearch(0, 4)
    assert result == [
        simple_graph.vertex[0],
        simple_graph.vertex[3],
        simple_graph.vertex[4],
    ]

    simple_graph.RemoveEdge(3, 4)
    result = simple_graph.BreadthFirstSearch(0, 4)
    assert result == []

    result = simple_graph.BreadthFirstSearch(0, 0)
    assert result == [simple_graph.vertex[0]]

    result = simple_graph.BreadthFirstSearch(0, 5)
    assert result == []

    result = simple_graph.BreadthFirstSearch(0, 2)
    assert result == [simple_graph.vertex[0], simple_graph.vertex[2]]
