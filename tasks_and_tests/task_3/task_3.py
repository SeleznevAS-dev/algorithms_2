from typing import Optional


class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey: int = key  # ключ узла
        self.NodeValue: int = val  # значение в узле
        self.Parent: Optional[BSTNode] = parent  # родитель или None для корня
        self.LeftChild: Optional[BSTNode] = None  # левый потомок
        self.RightChild: Optional[BSTNode] = None  # правый потомок


class BSTFind:  # промежуточный результат поиска
    def __init__(self):
        self.Node: Optional[BSTNode] = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:
    def __init__(self, node):
        self.Root: Optional[BSTNode] = node  # корень дерева, или None

    def FindNodeByKeyRecursive(self, find_class: BSTFind, key) -> BSTFind:
        if find_class.Node:
            node_key: int = find_class.Node.NodeKey
        else:
            return find_class

        if node_key == key:
            find_class.NodeHasKey = True

        elif node_key > key and find_class.Node.LeftChild:
            find_class.Node = find_class.Node.LeftChild
            return self.FindNodeByKeyRecursive(find_class, key)

        elif node_key > key and find_class.Node.LeftChild is None:
            find_class.ToLeft = True

        elif node_key < key and find_class.Node.RightChild:
            find_class.Node = find_class.Node.RightChild
            return self.FindNodeByKeyRecursive(find_class, key)

        return find_class

    def FindNodeByKey(self, key) -> BSTFind:
        find_class = BSTFind()
        if self.Root is None:
            return find_class

        find_class.Node = self.Root
        find_result: BSTFind = self.FindNodeByKeyRecursive(find_class, key)
        return find_result

    def AddKeyValue(self, key, val) -> bool:
        find_result: BSTFind = self.FindNodeByKey(key)

        if find_result.Node is None:
            self.Root = BSTNode(key, val, None)
            return True

        if find_result.NodeHasKey is True:
            return False  # если ключ уже есть

        if find_result.ToLeft is True:
            find_result.Node.LeftChild = BSTNode(key, val, find_result.Node)
            return True

        find_result.Node.RightChild = BSTNode(key, val, find_result.Node)
        return True

    def FinMinMax(self, FromNode: BSTNode, FindMax) -> BSTNode:
        if FindMax is True and FromNode.RightChild:
            return self.FinMinMax(FromNode.RightChild, FindMax)
        elif FindMax is False and FromNode.LeftChild:
            return self.FinMinMax(FromNode.LeftChild, FindMax)
        return FromNode

    def DeleteNodeFromParent(self, node: BSTNode) -> None:
        node_parent = node.Parent
        if node_parent is None:
            self.Root = None

        elif node_parent and node_parent.RightChild == node:
            node_parent.RightChild = None

        elif node_parent and node_parent.LeftChild == node:
            node_parent.LeftChild = None

    def ReplaceLeftNode(
        self, node_to_replace: BSTNode, node_for_replace: BSTNode
    ) -> None:
        node_parent = node_to_replace.Parent
        if node_parent is None:
            self.Root = node_for_replace
            node_for_replace.Parent = None

        elif node_parent and node_parent.RightChild == node_to_replace:
            node_parent.RightChild = node_for_replace
            node_for_replace.Parent = node_parent

        elif node_parent and node_parent.LeftChild == node_to_replace:
            node_parent.LeftChild = node_for_replace
            node_for_replace.Parent = node_parent

    def ReplaceRightNode(
        self, node_to_replace: BSTNode, node_for_replace: BSTNode
    ) -> None:
        assert node_for_replace.Parent
        if (
            node_for_replace.Parent.LeftChild
            and node_for_replace.Parent.LeftChild == node_for_replace
        ):
            node_for_replace.Parent.LeftChild = None

        elif (
            node_for_replace.Parent.RightChild
            and node_for_replace.Parent.RightChild == node_for_replace
        ):
            node_for_replace.Parent.RightChild = None

        node_to_replace.NodeKey, node_to_replace.NodeValue = (
            node_for_replace.NodeKey,
            node_for_replace.NodeValue,
        )

    def FindLeftChildRecursive(self, from_node: BSTNode) -> BSTNode:
        if from_node.LeftChild is None:
            return from_node

        return self.FindLeftChildRecursive(from_node.LeftChild)

    def DeleteNodeByKey(self, key) -> bool:
        # удаляем узел по ключу
        find_result: BSTFind = self.FindNodeByKey(key)
        if find_result.NodeHasKey is False or find_result.Node is None:
            return False  # если узел не найден
        if find_result.Node.RightChild is None and find_result.Node.LeftChild is None:
            self.DeleteNodeFromParent(find_result.Node)

        elif find_result.Node.RightChild is None and find_result.Node.LeftChild:
            self.ReplaceLeftNode(find_result.Node, find_result.Node.LeftChild)

        elif find_result.Node.RightChild:
            right_child = find_result.Node.RightChild
            node_for_replace = self.FindLeftChildRecursive(right_child)
            self.ReplaceRightNode(find_result.Node, node_for_replace)

        return True

    def CountRecursive(self, node: BSTNode, result: int) -> int:
        if node.LeftChild:
            result = self.CountRecursive(node.LeftChild, result + 1)
        if node.RightChild:
            result = self.CountRecursive(node.RightChild, result + 1)
        return result

    def Count(self) -> int:
        count_result = 0
        if not self.Root:
            return count_result

        return self.CountRecursive(self.Root, count_result + 1)

    def WideAllNodes(self) -> list[BSTNode]:
        assert self.Root
        node = self.Root
        result = [[node], []]
        level = 0
        while True:
            for next_node in result[level]:
                if next_node.LeftChild:
                    result[level + 1].append(next_node.LeftChild)
                if next_node.RightChild:
                    result[level + 1].append(next_node.RightChild)
            if result[level + 1] == []:
                break

            level += 1
            result.append([])

        final_result = []
        for i in result:
            final_result.extend(i)

        return final_result

    def DeepAllNodesRecursive(
        self, node: Optional[BSTNode], order: int, result: list[BSTNode]
    ) -> list[BSTNode]:
        if not node:
            return result

        if order == 0:
            result = self.DeepAllNodesRecursive(node.LeftChild, order, result)
            result.append(node)
            result = self.DeepAllNodesRecursive(node.RightChild, order, result)
        elif order == 1:
            result = self.DeepAllNodesRecursive(node.LeftChild, order, result)
            result = self.DeepAllNodesRecursive(node.RightChild, order, result)
            result.append(node)
        elif order == 2:
            result.append(node)
            result = self.DeepAllNodesRecursive(node.LeftChild, order, result)
            result = self.DeepAllNodesRecursive(node.RightChild, order, result)

        return result

    def DeepAllNodes(self, order: int) -> list[BSTNode]:
        return self.DeepAllNodesRecursive(self.Root, order, [])
