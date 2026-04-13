class Heap:
    def __init__(self):
        self.HeapArray: list[int | None] = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a: list[int], depth: int):
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        a.sort()
        a = a[::-1]
        heap_size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * heap_size

        index = 0
        for num in a:
            self.HeapArray[index] = num
            index += 1

    def SiftDown(self, index: int):
        if index >= len(self.HeapArray):
            return
        child_indexes = [2 * index + 1, 2 * index + 2]

        if child_indexes[0] >= len(self.HeapArray):
            return

        for _ in range(2):
            child_index = child_indexes.pop()
            if self.HeapArray[child_index] is not None:
                child_indexes.append(child_index)

        if child_indexes == []:
            return

        max_index = index
        for i in child_indexes:
            if (
                self.HeapArray[max_index] is not None
                and self.HeapArray[max_index] < self.HeapArray[i]  # ty:ignore
            ):
                max_index = i

        if max_index != index:
            self.HeapArray[index], self.HeapArray[max_index] = (
                self.HeapArray[max_index],
                self.HeapArray[index],
            )
            return self.SiftDown(max_index)

    def SiftUp(self, index: int):
        parent_index = int((index - 1) / 2)
        if parent_index < 0:
            return

        if self.HeapArray[parent_index] < self.HeapArray[index]:  # ty:ignore
            self.HeapArray[parent_index], self.HeapArray[index] = (
                self.HeapArray[index],
                self.HeapArray[parent_index],
            )
            self.SiftUp(parent_index)
            return

    def GetMax(self) -> int:
        max_element = self.HeapArray[0]
        # вернуть значение корня и перестроить кучу
        if max_element is None:
            return -1  # если куча пуста

        last_index = -1
        for i in range(len(self.HeapArray) - 1, -1, -1):
            if self.HeapArray[i] is not None:
                last_index = i
                break

        self.HeapArray[0], self.HeapArray[last_index] = self.HeapArray[last_index], None

        self.SiftDown(0)

        return max_element

    def Add(self, key) -> bool:
        # добавляем новый элемент key в кучу и перестраиваем её
        if self.HeapArray[-1] is not None:
            return False  # если куча вся заполнена

        free_index = self.HeapArray.index(None)
        self.HeapArray[free_index] = key

        self.SiftUp(free_index)

        return True
