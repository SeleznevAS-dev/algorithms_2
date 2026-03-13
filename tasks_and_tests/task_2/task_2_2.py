from .task_2 import BST, BSTNode


# Номер задания на курсе: 2
# Номер задачи из задания: 1
# Краткое название: BSTCheckIfEqual
# Сложность: Временная: O(n), Пространственная: O(n)


class BSTCheckIfEqual(BST):
    def CheckIfEqualRecursive(self, first_node: BSTNode, second_node: BSTNode) -> bool:
        if (
            first_node.NodeKey != second_node.NodeKey
            or first_node.NodeValue != second_node.NodeValue
        ):
            return False

        if (
            (first_node.LeftChild and second_node.LeftChild is None)
            or (first_node.LeftChild is None and second_node.LeftChild)
            or (first_node.RightChild and second_node.RightChild is None)
            or (first_node.RightChild is None and second_node.RightChild)
        ):
            return False

        is_equal = True

        if first_node.LeftChild and second_node.LeftChild:
            is_equal = self.CheckIfEqualRecursive(
                first_node.LeftChild, second_node.LeftChild
            )

        if not is_equal:
            return False

        if first_node.RightChild and second_node.RightChild:
            is_equal = self.CheckIfEqualRecursive(
                first_node.RightChild, second_node.RightChild
            )

        return is_equal

    def CheckIfEqual(self, second_bst: BST) -> bool:
        if self.Root is None or second_bst.Root is None:
            return False

        return self.CheckIfEqualRecursive(self.Root, second_bst.Root)


def test_check_if_equal():
    node_root = BSTNode(8, 8, None)
    bst = BSTCheckIfEqual(node_root)
    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)

    bst_2 = BSTCheckIfEqual(BSTNode(8, 8, None))
    bst_2.AddKeyValue(4, 4)
    bst_2.AddKeyValue(12, 12)
    bst_2.AddKeyValue(2, 2)
    bst_2.AddKeyValue(6, 6)

    assert bst.CheckIfEqual(bst_2) is True

    bst_2.AddKeyValue(10, 10)
    assert bst.CheckIfEqual(bst_2) is False


# Номер задания на курсе: 2
# Номер задачи из задания: 2
# Краткое название: BSTFindWayOfLength
# Сложность: Временная: O(n), Пространственная: O(n)


class BSTFindWayOfLength(BST):
    def FindWayOfLengthRecursive(
        self, node: BSTNode, result: list[list[BSTNode]], index: int, depth: int
    ):
        if result == []:
            result.append([])
        elif len(result) == index:
            result.append(result[index - 1][:depth])

        result[index].append(node)

        if node.LeftChild:
            result, index = self.FindWayOfLengthRecursive(
                node.LeftChild, result, index, depth + 1
            )

        if node.RightChild:
            result, index = self.FindWayOfLengthRecursive(
                node.RightChild, result, index, depth + 1
            )
        if node.LeftChild is None and node.RightChild is None:
            index += 1

        return result, index

    def FindWayOfLength(self, length: int) -> list[list[BSTNode]]:
        assert self.Root is not None
        return list(
            filter(
                lambda x: len(x) == length,
                self.FindWayOfLengthRecursive(self.Root, [], 0, 0)[0],
            )
        )


def test_find_way_of_length():
    node_root = BSTNode(8, 8, None)
    bst = BSTFindWayOfLength(node_root)
    assert len(bst.FindWayOfLength(1)) == 1

    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    assert len(bst.FindWayOfLength(2)) == 2

    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)
    assert len(bst.FindWayOfLength(3)) == 2


# Номер задания на курсе: 2
# Номер задачи из задания: 3
# Краткое название: BSTFindMaxWay
# Сложность: Временная: O(n), Пространственная: O(n)


class BSTFindMaxWay(BST):
    def FindMaxWayRecursive(
        self, node: BSTNode, result: list[list[BSTNode]], index: int, depth: int
    ):
        if result == []:
            result.append([])
        elif len(result) == index:
            result.append(result[index - 1][:depth])

        result[index].append(node)

        if node.LeftChild:
            result, index = self.FindMaxWayRecursive(
                node.LeftChild, result, index, depth + 1
            )

        if node.RightChild:
            result, index = self.FindMaxWayRecursive(
                node.RightChild, result, index, depth + 1
            )
        if node.LeftChild is None and node.RightChild is None:
            index += 1

        return result, index

    def FindMaxWay(self) -> list[list[BSTNode]]:
        assert self.Root is not None

        ways = self.FindMaxWayRecursive(self.Root, [], 0, 0)[0]

        sums = {i: 0 for i in range(len(ways))}
        for i, way in enumerate(ways):
            sm = 0
            for j in way:
                sm += j.NodeValue
            sums[i] = sm

        result = []
        max_value = max(sums.values())
        for key, value in sums.items():
            if value == max_value:
                result.append(ways[key])

        return result


def test_find_max_way():
    node_root = BSTNode(8, 8, None)
    bst = BSTFindMaxWay(node_root)
    assert len(bst.FindMaxWay()) == 1
    bst.AddKeyValue(7, 7)
    bst.AddKeyValue(9, 9)
    bst.AddKeyValue(2, 2)
    assert len(bst.FindMaxWay()) == 2


# Номер задания на курсе: 2
# Номер задачи из задания: 4
# Краткое название: BSTCheckIfSymmetry
# Сложность: Временная: O(n), Пространственная: O(n)


class BSTCheckIfSymmetry(BST):
    def CheckIfSymmetryRecursive(
        self, first_pointer: BSTNode, second_pointer: BSTNode
    ) -> bool:
        if (
            (first_pointer.LeftChild and second_pointer.RightChild is None)
            or (first_pointer.LeftChild is None and second_pointer.RightChild)
            or (first_pointer.RightChild and second_pointer.LeftChild is None)
            or (first_pointer.RightChild is None and second_pointer.LeftChild)
        ):
            return False

        is_symmetry = True

        if first_pointer.LeftChild and second_pointer.RightChild:
            is_symmetry = self.CheckIfSymmetryRecursive(
                first_pointer.LeftChild, second_pointer.RightChild
            )

        if not is_symmetry:
            return False

        if first_pointer.RightChild and second_pointer.LeftChild:
            is_symmetry = self.CheckIfSymmetryRecursive(
                first_pointer.RightChild, second_pointer.LeftChild
            )

        return is_symmetry

    def CheckIfSymmetry(self) -> bool:
        assert self.Root is not None

        if not self.Root.LeftChild or not self.Root.RightChild:
            return True

        return self.CheckIfSymmetryRecursive(self.Root.LeftChild, self.Root.RightChild)


def test_check_if_symmetry():
    node_root = BSTNode(8, 8, None)
    bst = BSTCheckIfSymmetry(node_root)
    assert bst.CheckIfSymmetry() is True

    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    assert bst.CheckIfSymmetry() is True

    bst.AddKeyValue(2, 2)
    assert bst.CheckIfSymmetry() is False

    bst.AddKeyValue(14, 14)
    assert bst.CheckIfSymmetry() is True
