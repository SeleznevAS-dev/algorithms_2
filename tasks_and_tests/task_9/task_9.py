class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:
    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode):
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete: SimpleTreeNode):
        if NodeToDelete.Parent is not None:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None

    def GetAllNodesRecursive(self, Node: SimpleTreeNode) -> list[SimpleTreeNode]:
        ans = [Node]
        node_childs = Node.Children
        for node_child in node_childs:
            ans.extend(self.GetAllNodesRecursive(node_child))

        return ans

    def GetAllNodes(self) -> list[SimpleTreeNode]:
        start_node = self.Root
        if start_node is None:
            return []

        return self.GetAllNodesRecursive(start_node)

    def FindNodesByValue(self, val) -> list[SimpleTreeNode]:
        nodes = self.GetAllNodes()
        return list(filter(lambda x: x.NodeValue == val, nodes))

    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self) -> int:
        return len(self.GetAllNodes())

    def LeafCount(self) -> int:
        nodes = self.GetAllNodes()
        return len(list(filter(lambda x: x.Children == [], nodes)))

    def CountSubtreeSizes(self, node: SimpleTreeNode, sizes: dict) -> int:
        current_size = 1

        for child in node.Children:
            child_size = self.CountSubtreeSizes(child, sizes)
            current_size += child_size

        sizes[node] = current_size
        return current_size

    def FindEdges(
        self, node: SimpleTreeNode, sizes: dict, result: list[SimpleTreeNode]
    ):
        for child in node.Children:
            if sizes[child] % 2 == 0:
                result.append(node)
                result.append(child)

            self.FindEdges(child, sizes, result)

    def EvenTrees(self) -> list[SimpleTreeNode | None]:
        result = []

        if self.Root is None:
            return result

        subtree_sizes = {}
        self.CountSubtreeSizes(self.Root, subtree_sizes)

        self.FindEdges(self.Root, subtree_sizes, result)

        return result
