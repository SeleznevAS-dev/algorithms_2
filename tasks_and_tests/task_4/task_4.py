import math


class aBST:
    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2 ** (depth + 1)
        self.Tree: list[int | None] = [None] * tree_size  # массив ключей

    def FindKeyIndexRecursive(self, current_index: int, key: int) -> int | None:
        if current_index >= len(self.Tree) - 1:
            return None

        tree_num = self.Tree[current_index]
        if tree_num is None:
            return -current_index

        elif tree_num == key:
            return current_index

        elif tree_num > key:
            next_index = (current_index * 2) + 1
            return self.FindKeyIndexRecursive(next_index, key)
        elif tree_num < key:
            next_index = (current_index * 2) + 2
            return self.FindKeyIndexRecursive(next_index, key)

    def FindKeyIndex(self, key) -> int | None:
        return self.FindKeyIndexRecursive(0, key)
        # ищем в массиве индекс ключа, None если не найден

    def AddKey(self, key) -> int:
        index = self.FindKeyIndex(key)
        if index is None:
            index = -1

        elif index == 0 and self.Tree[0] is None:
            self.Tree[index] = key

        elif index < 0:
            index = abs(index)
            self.Tree[index] = key

        return index
        # индекс добавленного/существующего ключа или -1 если не удалось

    def WideAllNodes(self) -> list[list]:
        result = []

        index = 0
        for level in range(int(math.sqrt(len(self.Tree) + 1))):
            result.append([])
            num_elements_on_level = 2**level
            for j in range(num_elements_on_level):
                result[level].append(self.Tree[index])
                index += 1

        return result
