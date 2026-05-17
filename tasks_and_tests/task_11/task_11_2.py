from .task_11 import SimpleGraph

# Номер задания на курсе: 11
# Номер задачи из задания: 2
# Краткое название: FindMaxLengthPath
# Сложность: Временная: O(N^3), Пространственная: O(N)


def FindMaxLengthPath(graph: SimpleGraph) -> int:
    result = 0

    for i in range(graph.max_vertex):
        for j in range(graph.max_vertex - i):
            bfs_result = graph.BreadthFirstSearch(i, j)
            if bfs_result and len(bfs_result) > result:
                result = len(bfs_result)

    return result


def test_FindMaxLengthPath():
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

    assert FindMaxLengthPath(simple_graph) == 3

    simple_graph.RemoveEdge(1, 4)

    assert FindMaxLengthPath(simple_graph) == 3

    simple_graph.RemoveEdge(3, 4)

    assert FindMaxLengthPath(simple_graph) == 3

    simple_graph.RemoveEdge(0, 1)

    assert FindMaxLengthPath(simple_graph) == 3


# Номер задания на курсе: 11
# Номер задачи из задания: 3
# Краткое название: FindAllCycles
# Сложность: Временная: O(N^3), Пространственная: O(N^2)


class FindAllCycles(SimpleGraph):
    def FindAllCycles(self) -> list:
        result = []

        for i in range(self.max_vertex):
            for j in range(self.max_vertex - i):
                if i == j:
                    continue

                if self.IsEdge(i, j):
                    self.RemoveEdge(i, j)
                    bfs_result = self.BreadthFirstSearch(i, j)

                    if bfs_result is not None:
                        result.append(bfs_result + [self.vertex[i]])
                self.AddEdge(i, j)

        result_indexes = []

        for cycle in result:
            result_indexes.append([self.vertex.index(vertex) for vertex in cycle])

        return result_indexes


def test_FindAllCycles():
    simple_graph = FindAllCycles(5)
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

    result = simple_graph.FindAllCycles()
    assert len(result) == 10


# Рефлексия.
# 1. Лес из чётных деревьев, из которого удалено максимально возможное количество рёбер.
# Сделал правильно.

# 2. Балансировка чётного двоичного дерева.
# Сделал почти так же: сортировал и перестраивал дерево.

# 3. Для любого заданного узла определить общее количество чётных поддеревьев.
# Сделал правильно.
