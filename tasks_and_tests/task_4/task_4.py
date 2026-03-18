import math


class aBST:
    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2 ** (depth + 1)
        self.Tree: list[int | None] = [None] * tree_size  # массив ключей

    def FindKeyIndexRecursive(self, current_index: int, key) -> int | None:
        if current_index >= len(self.Tree) - 1:
            return None

        tree_num = self.Tree[current_index]
        if self.Tree[current_index] is None or self.Tree[current_index] == key:
            return current_index

        if tree_num > key:
            next_index = (current_index * 2) + 1
            return self.FindKeyIndexRecursive(next_index, key)
        elif tree_num < key:
            next_index = (current_index * 2) + 2
            return self.FindKeyIndexRecursive(next_index, key)

    def FindKeyIndex(self, key) -> int | None:
        # ищем в массиве индекс ключа, None если не найден
        return self.FindKeyIndexRecursive(0, key)

    def AddKey(self, key) -> int:
        found_key = self.FindKeyIndex(key)
        if found_key is not None:
            self.Tree[found_key] = key
        else:
            found_key = -1
        return found_key
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
