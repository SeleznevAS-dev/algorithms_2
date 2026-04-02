from typing import Optional
from .task_6 import BalancedBST, BSTNode

# Номер задания на курсе: 6
# Номер задачи из задания: 2
# Краткое название: IsTreeCorrect
# Сложность: Временная: O(N), Пространственная: O(H)


def IsTreeCorrectRecursive(node: BSTNode) -> bool:
    node_key = node.NodeKey
    if node.LeftChild and not IsTreeCorrectRecursive(node.LeftChild):
        return False
    if node.LeftChild and node.LeftChild.NodeKey >= node_key:
        return False

    if node.RightChild and not IsTreeCorrectRecursive(node.RightChild):
        return False
    if node.RightChild and node.RightChild.NodeKey < node_key:
        return False

    return True


def IsTreeCorrect(tree: BalancedBST) -> bool:
    assert tree.Root
    return IsTreeCorrectRecursive(tree.Root)


def test_is_tree_correct():
    tree = BalancedBST()
    tree.GenerateTree([1, 2, 3, 4, 5, 6, 7])
    assert IsTreeCorrect(tree)

    tree.Root.LeftChild.NodeKey = 10
    assert not IsTreeCorrect(tree)


# Номер задания на курсе: 6
# Номер задачи из задания: 2
# Краткое название: IsBalanced
# Сложность: Временная: O(N), Пространственная: O(H)
# Задание под звездочкой, но есть и в основном решении.


class IsBalancedBST(BalancedBST):
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
        return is_balanced


def test_is_balanced():
    tree = IsBalancedBST()
    tree.GenerateTree([4, 2, 6, 1])
    assert tree.IsBalanced(tree.Root)

    tree.Root.LeftChild.LeftChild.RightChild = BSTNode(0, tree.Root.LeftChild.LeftChild)
    assert not tree.IsBalanced(tree.Root)


# Рефлексия.
# 2. Поиск наименьшего общего предка (LCA).
# Сделал без рекурсии, по индексам массива в направлении от листьев к корню.

# 3. Оптимизированный метод обхода дерева в ширину.
# Сделал без очереди, шёл по уроням, добавляя элементы в результат.
