from typing import Optional
from .task_8 import Vertex, SimpleGraph

# Номер задания на курсе: 8
# Номер задачи из задания: 2
# Краткое название: IsCycle
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

    def IsCycleRecursive(self, start_index: int, current_index: int) -> bool:
        next_indexes = []
        for i in range(len(self.m_adjacency[current_index])):
            if self.m_adjacency[current_index][i][1] == 1 and i == start_index:
                return True
            elif self.m_adjacency[current_index][i][1] == 1:
                next_indexes.append(i)

        for j in next_indexes:
            result = self.IsCycleRecursive(start_index, j)
            if result is True:
                return True

        return False

    def IsCycle(self) -> bool:
        for i in range(len(self.vertex)):
            if self.vertex[i] is not None:
                result = self.IsCycleRecursive(i, i)
            if result is True:
                return True

        return False


def test_directed_graph_is_cycle():
    graph = DirectedGraph(5)
    graph.AddVertex(1)
    graph.AddVertex(2)
    graph.AddVertex(3)
    graph.AddEdge(0, 1, 1)
    graph.AddEdge(1, 2, 1)
    assert graph.IsCycle() is False
    graph.AddEdge(2, 0, 1)
    assert graph.IsCycle() is True


# Рефлексия.
# 2. Проверка, правильно ли распределены значения в двоичном дереве .
# Сделал полностью правильно.

# 3. Проверка, сбалансировано ли двоичное дерево .
# Сделал немного не так: высота считалась 0 в корне, у листьев высота была максимальной. Получается, вычислял конкретную высоту только после проверки поддеревьев.
