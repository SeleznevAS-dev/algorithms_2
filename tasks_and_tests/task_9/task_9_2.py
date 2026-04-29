from typing import Optional
from .task_9 import SimpleTree, SimpleTreeNode

# Номер задания на курсе: 9
# Номер задачи из задания: 2
# Краткое название: BalanceEvenBinaryTree
# Сложность: Временная: O(N log N), Пространственная: O(N)


class BalancedTree(SimpleTree):
    def BuildBalancedTree(
        self,
        sorted_nodes: list,
        left: int,
        right: int,
        parent: Optional[SimpleTreeNode] = None,
    ) -> Optional[SimpleTreeNode]:
        if left > right:
            return None

        mid = (left + right) // 2
        node = sorted_nodes[mid]

        node.Children = []
        node.Parent = parent

        left_child = self.BuildBalancedTree(sorted_nodes, left, mid - 1, node)
        right_child = self.BuildBalancedTree(sorted_nodes, mid + 1, right, node)

        if left_child:
            node.Children.append(left_child)
        if right_child:
            node.Children.append(right_child)

        return node

    def BalanceBinaryTree(self):
        if self.Root is None:
            return

        all_nodes = self.GetAllNodes()

        all_nodes.sort(key=lambda x: x.NodeValue)

        self.Root = self.BuildBalancedTree(all_nodes, 0, len(all_nodes) - 1)


def test_BalanceBinaryTree():
    root = SimpleTreeNode(1, None)
    node2 = SimpleTreeNode(2, root)
    node3 = SimpleTreeNode(3, node2)
    node4 = SimpleTreeNode(4, node3)
    node5 = SimpleTreeNode(5, node4)

    root.Children = [node2]
    node2.Children = [node3]
    node3.Children = [node4]
    node4.Children = [node5]

    tree = BalancedTree(root)

    assert tree.Root.NodeValue == 1
    assert tree.Root.Children[0].NodeValue == 2
    assert tree.Root.Children[0].Children[0].NodeValue == 3
    assert tree.Root.Children[0].Children[0].Children[0].NodeValue == 4
    assert tree.Root.Children[0].Children[0].Children[0].Children[0].NodeValue == 5

    tree.BalanceBinaryTree()
    assert tree.Root.NodeValue == 3
    assert tree.Root.Children[0].NodeValue == 1
    assert tree.Root.Children[1].NodeValue == 4
    assert tree.Root.Children[0].Children[0].NodeValue == 2
    assert tree.Root.Children[1].Children[0].NodeValue == 5


# Номер задания на курсе: 9
# Номер задачи из задания: 3
# Краткое название: CountEvenSubtrees
# Сложность: Временная: O(N), Пространственная: O(N)


def CountEvenSubtrees(node: SimpleTreeNode, tree: SimpleTree) -> int:
    subtree_sizes = {}
    tree.CountSubtreeSizes(node, subtree_sizes)
    even_subtree_count = 0
    for size in subtree_sizes.values():
        if size % 2 == 0:
            even_subtree_count += 1

    return even_subtree_count


def test_CountEvenSubtrees():
    root = SimpleTreeNode(1, None)
    node2 = SimpleTreeNode(2, root)
    node3 = SimpleTreeNode(3, root)
    node4 = SimpleTreeNode(4, node2)
    node5 = SimpleTreeNode(5, node2)
    node6 = SimpleTreeNode(6, node3)

    tree = SimpleTree(root)

    tree.AddChild(root, node2)
    tree.AddChild(root, node3)
    tree.AddChild(node2, node4)
    tree.AddChild(node2, node5)
    tree.AddChild(node3, node6)

    assert CountEvenSubtrees(node2, tree) == 0
    assert CountEvenSubtrees(node3, tree) == 1


# Рефлексия.
# 4. Поиск максимального элемента в заданном диапазоне значений.
# Сделал правильно через цикл по массиву.

# 5. Предикативный поиск.
# Описал правильно.

# 6. Объединение текущей кучи с кучей-параметром.
# Не до конца понял суть и решение задачи.
