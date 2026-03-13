from .task_3 import BST, BSTNode


# Номер задания на курсе: 3
# Номер задачи из задания: 3
# Краткое название: BSTInvertTree
# Сложность: Временная: O(n), Пространственная: O(n)


class BSTInvertTree(BST):
    def InvertTree(self) -> list[BSTNode]:
        assert self.Root

        node = self.Root
        result = [[node], []]
        level = 0
        keys_values = [node.NodeKey]
        while True:
            keys_values = keys_values[::-1]
            for next_node in result[level]:
                next_node.NodeKey = keys_values.pop(0)
                next_node.NodeValue = next_node.NodeKey
                if next_node.LeftChild:
                    result[level + 1].append(next_node.LeftChild)
                    keys_values.append(next_node.LeftChild.NodeKey)
                if next_node.RightChild:
                    result[level + 1].append(next_node.RightChild)
                    keys_values.append(next_node.RightChild.NodeKey)

            if result[level + 1] == []:
                break

            level += 1
            result.append([])

        final_result = []
        for i in result:
            final_result.extend(i)

        return final_result


def test_invert_tree():
    node_root = BSTNode(8, 8, None)
    bst = BSTInvertTree(node_root)
    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)

    all_nodes = bst.InvertTree()
    assert all_nodes[0].NodeValue == 8
    assert all_nodes[1].NodeValue == 12
    assert all_nodes[2].NodeValue == 4
    assert all_nodes[3].NodeValue == 6
    assert all_nodes[4].NodeValue == 2


# Номер задания на курсе: 3
# Номер задачи из задания: 4
# Краткое название: BSTMaxLevelTree
# Сложность: Временная: O(n), Пространственная: O(n)
# Можно оптимизировать решение если в теории как-то учитывать что дерево бинарное и заранее отметать уровни, на которых не может быть максимума


class BSTMaxLevelTree(BST):
    def FindMaxWideValues(self) -> int:
        assert self.Root
        node = self.Root

        nodes_list = [[node], []]
        level = 0
        max_sum = node.NodeValue
        max_sum_level = level
        while True:
            sum_level = 0
            for next_node in nodes_list[level]:
                sum_level += next_node.NodeValue
                if next_node.LeftChild:
                    nodes_list[level + 1].append(next_node.LeftChild)
                if next_node.RightChild:
                    nodes_list[level + 1].append(next_node.RightChild)

            if sum_level >= max_sum:
                max_sum = sum_level
                max_sum_level = level

            if nodes_list[level + 1] == []:
                break

            level += 1
            nodes_list.append([])

        return max_sum_level


def test_find_max_wide_values():
    node_root = BSTNode(8, 8, None)
    bst = BSTMaxLevelTree(node_root)
    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)

    assert bst.FindMaxWideValues() == 1

    bst.AddKeyValue(10, 10)
    assert bst.FindMaxWideValues() == 2


# Номер задания на курсе: 3
# Номер задачи из задания: 5
# Краткое название: RecoverTree
# Сложность: Временная: O(n), Пространственная: O(n)
# Обязательно нужны оба обхода для однозначного восстановления дерева, так как по одному обходу может быть несколько вариантов дерева


def RecoverTree(prefix_keys: list[int], infix_keys: list[int]) -> BST:
    if not prefix_keys or not infix_keys:
        return BST(None)
    elif len(prefix_keys) == 1 and len(infix_keys) == 1:
        return BST(BSTNode(prefix_keys[0], prefix_keys[0], None))

    root_key = prefix_keys[0]
    root = BSTNode(root_key, root_key, None)

    root_index = infix_keys.index(root_key)

    left_infix = infix_keys[:root_index]
    right_infix = infix_keys[root_index + 1 :]

    left_prefix = prefix_keys[1 : 1 + len(left_infix)]
    right_prefix = prefix_keys[1 + len(left_infix) :]

    if left_prefix:
        left_subtree = RecoverTree(left_prefix, left_infix)
        if left_subtree.Root:
            root.LeftChild = left_subtree.Root
            root.LeftChild.Parent = root

    if right_prefix:
        right_subtree = RecoverTree(right_prefix, right_infix)
        if right_subtree.Root:
            root.RightChild = right_subtree.Root
            root.RightChild.Parent = root

    return BST(root)


def test_recover_tree():
    bst = BST(BSTNode(8, 8, None))
    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)
    bst.AddKeyValue(10, 10)
    bst.AddKeyValue(14, 14)

    prefix_result = bst.DeepAllNodes(2)
    infix_result = bst.DeepAllNodes(0)

    prefix_keys = [node.NodeKey for node in prefix_result]
    infix_keys = [node.NodeKey for node in infix_result]

    recovered_tree = RecoverTree(prefix_keys, infix_keys)

    for i in range(len(prefix_result)):
        assert prefix_result[i].NodeKey == recovered_tree.DeepAllNodes(2)[i].NodeKey
        assert infix_result[i].NodeKey == recovered_tree.DeepAllNodes(0)[i].NodeKey
