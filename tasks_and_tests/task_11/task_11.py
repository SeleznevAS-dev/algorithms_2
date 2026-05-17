class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item  # type: ignore

        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is None:
            print(node.value)  # type: ignore
            node = node.next  # type: ignore

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head
        node_prev = self.head

        while node is not None:
            if node.value == val and node == self.head and node == self.tail:
                self.head = None
                self.tail = None
                break

            elif node.value == val and node != self.tail and node != self.head:
                node_prev.next = node.next  # type: ignore
                node = node_prev
                if all is False:
                    break

            elif node.value == val and node == self.head:
                self.head = node.next
                node = node.next

            elif node.value == val and node == self.tail:
                node_prev.next = None  # type: ignore
                self.tail = node_prev
                break

            node_prev = node
            node = node.next  # type: ignore

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        result = 0
        node = self.head
        while node is not None:
            result += 1
            node = node.next
        return result

    def insert(self, afterNode, newNode):
        if afterNode is None and self.tail is None:
            newNode.next = self.head
            self.head = newNode
            self.tail = newNode
            return

        if afterNode is None:
            return

        prev_next = afterNode.next
        newNode.next = prev_next
        afterNode.next = newNode

        if prev_next is None:
            self.tail = newNode


class Queue:
    def __init__(self):
        self.queue = LinkedList()
        self.queue_size = 0

    # Complexity: time: O(1), space: O(1)
    def enqueue(self, item):
        node = Node(item)
        self.queue.add_in_tail(node)
        self.queue_size += 1

    # Complexity: time: O(1), space: O(1)
    def dequeue(self):
        if self.queue.head is not None:
            node = self.queue.head
            self.queue.head = node.next
            self.queue_size -= 1
            return node.value
        return None

    def size(self):
        return self.queue_size


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

    def BreadthFirstSearch(self, VFrom: int, VTo: int):
        VFrom_start = VFrom
        result = []

        if VFrom < 0 or VFrom >= self.max_vertex or VTo < 0 or VTo >= self.max_vertex:
            return result

        if self.vertex[VFrom] is None or self.vertex[VTo] is None:
            return result

        if VFrom == VTo:
            return [self.vertex[VFrom]]

        queue = Queue()
        for i in range(self.max_vertex):
            if self.vertex[i] is not None and self.vertex[i].Hit is True:  # type: ignore
                self.vertex[i].Hit = False  # type: ignore

        queue.enqueue(VFrom)

        queue_history = []

        while True:
            is_found = False
            if queue.size() == 0:
                break

            VFrom = queue.dequeue()
            if self.vertex[VFrom].Hit is True:
                continue

            queue_history.append(VFrom)

            for i in range(self.max_vertex):
                if i == VFrom:
                    continue

                if self.m_adjacency[VFrom][i] == 0:
                    continue

                if (
                    self.vertex[i].Hit is False  # type: ignore
                    and i == VTo
                ):
                    self.vertex[VTo].Hit = True  # type: ignore
                    queue_history.append(i)
                    is_found = True
                    break

                elif (
                    self.vertex[i].Hit is False  # type: ignore
                ):
                    queue.enqueue(i)

            self.vertex[VFrom].Hit = True

            if is_found is True:
                break

        if is_found is False:
            return result

        VFrom = VFrom_start

        while VTo != VFrom:
            last_queue = queue_history.pop(-1)
            for i in queue_history:
                if self.m_adjacency[last_queue][i] == 1:
                    result.append(self.vertex[last_queue])
                    VTo = i
                    break

        result.append(self.vertex[VTo])

        result = result[::-1]

        return result
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
