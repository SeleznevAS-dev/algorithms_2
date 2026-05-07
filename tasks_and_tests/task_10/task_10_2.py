from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "task_10"))

from .task_10 import SimpleGraph, Vertex

# Номер задания на курсе: 10
# Номер задачи из задания: 1
# Краткое название: IsSimpleGraphLinked
# Сложность: Временная: O(N^2), Пространственная: O(N)


class IsSimpleGraphLinked(SimpleGraph):
    def CheckIsSimpleGraphLinked(self) -> bool:
        combinations = set()
        for i in range(self.max_vertex):
            for j in range(self.max_vertex):
                if self.vertex[i] is None or self.vertex[j] is None:
                    continue

                if i == j:
                    continue

                result = None
                if (i, j) not in combinations:
                    result = self.DepthFirstSearch(i, j)
                    combinations.add((i, j))
                    combinations.add((j, i))

                if result == []:
                    return False

        return True


def test_IsSimpleGraphLinked():
    simple_graph = IsSimpleGraphLinked(5)
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

    assert simple_graph.CheckIsSimpleGraphLinked() is True

    simple_graph.RemoveEdge(1, 4)

    assert simple_graph.CheckIsSimpleGraphLinked() is True

    simple_graph.RemoveEdge(3, 4)

    assert simple_graph.CheckIsSimpleGraphLinked() is False

    simple_graph.RemoveVertex(4)

    assert simple_graph.CheckIsSimpleGraphLinked() is True


# Номер задания на курсе: 10
# Номер задачи из задания: 2
# Краткое название: FindMaxSimplePathLen
# Сложность: Временная: O(N^2), Пространственная: O(N)


class DirectedGraph(SimpleGraph):
    def __init__(self, size):
        self.max_vertex: int = size
        self.m_adjacency: list[list[tuple[int, int]]] = [
            [(0, 0)] * size for _ in range(size)
        ]
        self.vertex: list[Vertex | None] = [None] * size

    def IsEdge(self, v1: int, v2: int) -> bool:
        # True если есть ребро между вершинами v1 и v2
        if self.m_adjacency[v1][v2][0] == 1 and self.m_adjacency[v2][v1][0] == 1:
            return True
        return False

    def AddEdge(self, v1: int, v2: int, direction: Optional[int] = None) -> None:
        # добавление ребра между вершинами v1 и v2
        if not direction:
            self.m_adjacency[v1][v2], self.m_adjacency[v2][v1] = (
                (1, 0),
                (1, 0),
            )
            return

        self.m_adjacency[v1][v2], self.m_adjacency[v2][v1] = (
            (1, direction),
            (1, -direction),
        )

    def RemoveEdge(self, v1: int, v2: int) -> None:
        # удаление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2], self.m_adjacency[v2][v1] = (0, 0), (0, 0)

    def FindMaxPathLenRecursive(self, index: int, current_path: set) -> int:
        current_path.add(index)
        next_indexes = []
        for i in range(len(self.m_adjacency[index])):
            if self.m_adjacency[index][i][1] == 1 and i not in current_path:
                next_indexes.append(i)

        max_path_len = 0
        for j in next_indexes:
            path_len = self.FindMaxPathLenRecursive(j, current_path)
            if path_len > max_path_len:
                max_path_len = path_len

        current_path.remove(index)
        return max_path_len + 1

    def FindMaxSimplePathLen(self) -> int:
        max_path_len = 0
        for i in range(len(self.vertex)):
            path_len = 0
            if self.vertex[i] is not None:
                path_len = self.FindMaxPathLenRecursive(i, set())
            if path_len > max_path_len:
                max_path_len = path_len

        return max_path_len


def test_FindMaxSimplePathLen():
    directed_graph = DirectedGraph(5)
    directed_graph.AddVertex(1)
    directed_graph.AddVertex(2)
    directed_graph.AddVertex(3)
    directed_graph.AddVertex(4)
    directed_graph.AddVertex(5)
    directed_graph.AddEdge(0, 1, 1)  # A -> B
    directed_graph.AddEdge(0, 2, 1)  # A -> C
    directed_graph.AddEdge(0, 3, 1)  # A -> D
    directed_graph.AddEdge(1, 3, 1)  # B -> D
    directed_graph.AddEdge(1, 4, 1)  # B -> E
    directed_graph.AddEdge(2, 3, 1)  # C -> D
    directed_graph.AddEdge(3, 3, 1)  # D -> D
    directed_graph.AddEdge(3, 4, 1)  # D -> E

    assert directed_graph.FindMaxSimplePathLen() == 4

    directed_graph.RemoveEdge(3, 4)

    assert directed_graph.FindMaxSimplePathLen() == 3

    directed_graph.RemoveEdge(1, 4)

    assert directed_graph.FindMaxSimplePathLen() == 3

    directed_graph.RemoveEdge(0, 3)

    assert directed_graph.FindMaxSimplePathLen() == 3

    directed_graph.RemoveEdge(1, 3)

    assert directed_graph.FindMaxSimplePathLen() == 3

    directed_graph.RemoveEdge(2, 3)

    assert directed_graph.FindMaxSimplePathLen() == 2


# Рефлексия.
# 2. Направленный граф, представленный матрицей смежности.
# Не стал менять размер матрицы, чтобы не усложнять код. Проверял, была ли возможность по направлениям вернуться к начальному индексу. Не ошибка, просто другое решение.
