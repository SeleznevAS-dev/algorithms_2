from typing import Optional


class BSTNode:
    def __init__(self, key, parent):
        self.NodeKey: int = key  # ключ узла
        self.Parent: Optional[BSTNode] = parent  # родитель или None для корня
        self.LeftChild: Optional[BSTNode] = None  # левый потомок
        self.RightChild: Optional[BSTNode] = None  # правый потомок
        self.Level: int = 0  # уровень узла


class BalancedBST:
    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTreeRecursive(
        self, parent_node: Optional[BSTNode], a: list[int], level: int
    ) -> Optional[BSTNode]:
        if a == []:
            return

        middle_index = len(a) // 2
        node = BSTNode(a[middle_index], parent_node)
        node.Level = level

        left_part = a[:middle_index]
        right_part = a[middle_index + 1 :]

        node.LeftChild = self.GenerateTreeRecursive(node, left_part, level + 1)

        node.RightChild = self.GenerateTreeRecursive(node, right_part, level + 1)

        return node

    def GenerateTree(self, a: list[int]) -> None:
        # создаём дерево с нуля из неотсортированного массива a
        a.sort()
        self.Root = self.GenerateTreeRecursive(None, a, 0)

    def IsBalancedRecursive(
        self, node: Optional[BSTNode], height: int
    ) -> tuple[bool, int]:
        if not node:
            return True, height - 1

        is_left_balanced, left_height = self.IsBalancedRecursive(
            node.LeftChild, height + 1
        )

        if not is_left_balanced:
            return False, height

        is_right_balanced, right_height = self.IsBalancedRecursive(
            node.RightChild, height + 1
        )

        max_height = max(left_height, right_height)

        if not is_left_balanced or not is_right_balanced:
            return False, max_height

        if abs(left_height - right_height) > 1:
            return False, max_height

        return True, max_height

    def IsBalanced(self, root_node) -> bool:
        is_balanced, _ = self.IsBalancedRecursive(root_node, 0)
        return is_balanced  # сбалансировано ли дерево с корнем root_node
