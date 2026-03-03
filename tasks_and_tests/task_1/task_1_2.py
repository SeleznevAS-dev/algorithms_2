from .task_1 import SimpleTreeNode, SimpleTree


# Номер задания на курсе: 1
# Номер задачи из задания: 1
# Краткое название: GetAllNodesWithLevels
# Сложность: Временная: O(n), Пространственная: O(n)


class SimpleTreeWithLevels(SimpleTree):
    def GetAllNodesWithLevelsRecursive(self, Node: SimpleTreeNode, level: int):
        ans = [(Node, level)]
        node_childs = Node.Children
        for node_child in node_childs:
            ans.extend(self.GetAllNodesWithLevelsRecursive(node_child, level + 1))

        return ans

    def GetAllNodesWithLevels(self):
        start_node = self.Root
        if start_node is None:
            return []

        return self.GetAllNodesWithLevelsRecursive(start_node, 0)


def test_GetAllNodesWithLevels():
    node = SimpleTreeNode(1, None)
    tree = SimpleTreeWithLevels(node)
    child_node1 = SimpleTreeNode(2, None)
    child_node2 = SimpleTreeNode(3, None)
    tree.AddChild(node, child_node1)
    tree.AddChild(node, child_node2)
    all_nodes_with_levels = tree.GetAllNodesWithLevels()
    assert (node, 0) in all_nodes_with_levels
    assert (child_node1, 1) in all_nodes_with_levels
    assert (child_node2, 1) in all_nodes_with_levels


# Номер задания на курсе: 1
# Номер задачи из задания: 2
# Краткое название: SimpleTreeNodeWithLevels
# Идея в том, чтобы хранить уровень в классе узла, таким образом всегда будет доступ к нему всегда будет доступ.

class SimpleTreeNodeWithLevels(SimpleTreeNode):
    def __init__(self, val, parent):
        super().__init__(val, parent)
        self.level = 0


class SimpleTreeWithLevelsSecond(SimpleTree):
    def AddChild(self, ParentNode, NewChild):
        NewChild.level = ParentNode.level + 1
        return super().AddChild(ParentNode, NewChild)


def test_SimpleTreeNodeWithLevels():
    node = SimpleTreeNodeWithLevels(1, None)
    tree = SimpleTreeWithLevelsSecond(node)
    child_node1 = SimpleTreeNodeWithLevels(2, None)
    child_node2 = SimpleTreeNodeWithLevels(3, None)
    tree.AddChild(node, child_node1)
    tree.AddChild(node, child_node2)
    assert node.level == 0
    assert child_node1.level == 1
    assert child_node2.level == 1
