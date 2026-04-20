from .task_8 import SimpleGraph


def test_add_vertex():
    graph = SimpleGraph(5)
    graph.AddVertex(1)
    graph.AddVertex(2)
    graph.AddVertex(3)
    assert graph.vertex[0] is not None and graph.vertex[0].Value == 1
    assert graph.vertex[1] is not None and graph.vertex[1].Value == 2
    assert graph.vertex[2] is not None and graph.vertex[2].Value == 3
    assert graph.vertex[3] is None
    assert graph.vertex[4] is None


def test_remove_vertex():
    graph = SimpleGraph(5)
    graph.AddVertex(1)
    graph.AddVertex(2)
    graph.AddVertex(3)
    graph.RemoveVertex(1)
    assert graph.vertex[0] is not None and graph.vertex[0].Value == 1
    assert graph.vertex[1] is None
    assert graph.vertex[2] is not None and graph.vertex[2].Value == 3
    assert graph.vertex[3] is None
    assert graph.vertex[4] is None


def test_add_edge():
    graph = SimpleGraph(5)
    graph.AddVertex(1)
    graph.AddVertex(2)
    graph.AddEdge(0, 1)
    assert graph.IsEdge(0, 1) == 1
    assert graph.IsEdge(1, 0) == 1
    assert graph.IsEdge(0, 2) == 0
    assert graph.IsEdge(1, 2) == 0


def test_remove_edge():
    graph = SimpleGraph(5)
    graph.AddVertex(1)
    graph.AddVertex(2)
    graph.AddEdge(0, 1)
    graph.RemoveEdge(0, 1)
    assert graph.IsEdge(0, 1) == 0
    assert graph.IsEdge(1, 0) == 0


def test_is_edge():
    graph = SimpleGraph(5)
    graph.AddVertex(1)
    graph.AddVertex(2)
    graph.AddEdge(0, 1)
    assert graph.IsEdge(0, 1) is True
    assert graph.IsEdge(1, 0) is True
    assert graph.IsEdge(0, 2) is False
    assert graph.IsEdge(1, 2) is False
