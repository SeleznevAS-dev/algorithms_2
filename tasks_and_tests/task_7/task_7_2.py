from .task_7 import Heap

# Номер задания на курсе: 7
# Номер задачи из задания: 4
# Краткое название: FindMaxInRange
# Сложность: Временная: O(N), Пространственная: O(1)


def FindMaxInRange(heap: Heap, range: tuple[int, int]) -> int | None:
    range_min = range[0]
    range_max = range[1]
    max_element = None
    for i in heap.HeapArray:
        if i is not None and (
            (i <= range_max and i >= range_min)
            and (max_element is None or (i >= max_element))
        ):
            max_element = i

    return max_element


def test_find_max_in_range():
    heap = Heap()
    heap.MakeHeap([1, 2, 3, 4, 5, 6, 7], 2)
    assert FindMaxInRange(heap, (2, 5)) == 5
    assert FindMaxInRange(heap, (0, 1)) == 1
    assert FindMaxInRange(heap, (6, 10)) == 7
    assert FindMaxInRange(heap, (8, 10)) is None


# Номер задания на курсе: 7
# Номер задачи из задания: 5
# Краткое название: BestSearchAlgorithmWithCondition
# Известно, что ключи наследников должны быть меньше ключа родителя. Тогда можно рекурсивно проходиться по всем веткам сверху вниз и если родитель или потомки не подходят по условиям, то прекращать прохождение дальше вглубь по этой ветке.


# Номер задания на курсе: 7
# Номер задачи из задания: 6
# Краткое название: JoinTwoHeaps
# Сложность: Временная: O(N), Пространственная: O(1)
class HeapWithJoin(Heap):
    def JoinTwoHeaps(self, heap2: Heap):
        while heap2.HeapArray[0] is not None:
            max_element = heap2.GetMax()
            self.Add(max_element)


def test_join_two_heaps():
    heap1 = HeapWithJoin()
    heap1.MakeHeap([1, 2, 3], 2)
    heap2 = HeapWithJoin()
    heap2.MakeHeap([4, 5, 6], 2)

    heap1.JoinTwoHeaps(heap2)
    assert heap1.HeapArray == [6, 5, 4, 1, 3, 2, None]


# Рефлексия.
# 2. Эффективность поиска узла в дереве, представленном в виде массива.
# Оценил так же, хотя есть различия, в зависимости от того, насколько заполнено дерево.

# 3. Удаление узла из двоичного дерева, заданного в виде массива.
# Реализовал просто и очень плохо, через массив, хотя стоило бы применить изученное в этом занятии просеивание и выполнять его.

# 4. Сортировка двоичного дерева за O(1)
# Полностью правильно.
