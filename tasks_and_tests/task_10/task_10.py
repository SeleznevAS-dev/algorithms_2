from typing import Optional


class Stack:
    def __init__(self):
        self.stack = []

    def add(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop(-1)
        return None

    def __len__(self):
        return len(self.stack)


class Vertex:
    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:
    def __init__(self, size):
        self.max_vertex: int = size
        self.m_adjacency: list[list[int]] = [[0] * size for _ in range(size)]
        self.vertex: list[Vertex | None] = [None] * size

    def AddVertex(self, v: int) -> None:
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        free_index = self.vertex.index(None)
        if free_index is not None:
            self.vertex[free_index] = Vertex(v)

    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v: int) -> None:
        # ваш код удаления вершины со всеми её рёбрами
        self.vertex[v] = None
        self.m_adjacency[v] = [0] * self.max_vertex
        for i in range(self.max_vertex):
            self.m_adjacency[i][v] = 0

    def IsEdge(self, v1: int, v2: int) -> bool:
        # True если есть ребро между вершинами v1 и v2
        if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1:
            return True
        return False

    def AddEdge(self, v1: int, v2: int) -> None:
        # добавление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2], self.m_adjacency[v2][v1] = 1, 1

    def RemoveEdge(self, v1: int, v2: int) -> None:
        # удаление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2], self.m_adjacency[v2][v1] = 0, 0

    def DepthFirstSearchRecursive(
        self, VFrom: int, VTo: int, stack: Stack, add_to_stack: bool
    ) -> Optional[Stack]:

        self.vertex[VFrom].Hit = True  # type: ignore
        if add_to_stack is True:
            stack.add(VFrom)

        for i in range(self.max_vertex):
            if self.m_adjacency[VFrom][i] == 1 and i == VTo:
                stack.add(VTo)
                return stack

        for i in range(self.max_vertex):
            found_stack = None
            if (
                self.m_adjacency[VFrom][i] == 1
                and self.vertex[i] is not None
                and self.vertex[i].Hit is False  # type: ignore
            ):
                found_stack = self.DepthFirstSearchRecursive(i, VTo, stack, True)

            if found_stack is not None:
                return stack

        while len(stack) > 0:
            if (
                self.DepthFirstSearchRecursive(stack.pop(), VTo, stack, False)
                is not None
            ):
                return stack

        return stack

    def DepthFirstSearch(self, VFrom: int, VTo: int) -> Optional[list[Vertex]]:
        result = []
        stack = Stack()

        if VFrom < 0 or VFrom >= self.max_vertex or VTo < 0 or VTo >= self.max_vertex:
            return result

        if self.vertex[VFrom] is None or self.vertex[VTo] is None:
            return result

        if VFrom == VTo:
            return [self.vertex[VFrom]]  # type: ignore

        for i in range(self.max_vertex):
            if self.vertex[i] is not None and self.vertex[i].Hit is True:  # type: ignore
                self.vertex[i].Hit = False  # type: ignore

        self.DepthFirstSearchRecursive(VFrom, VTo, stack, True)

        while len(stack) > 0:
            result.append(self.vertex[stack.pop()])

        result = result[::-1]

        return result
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
