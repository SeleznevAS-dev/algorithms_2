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

    def GetAllNodesRecursive(self, Node: SimpleTreeNode):
        ans = [Node]
        node_childs = Node.Children
        for node_child in node_childs:
            ans.extend(self.GetAllNodesRecursive(node_child))

        return ans

    def GetAllNodes(self):
        start_node = self.Root
        if start_node is None:
            return []

        return self.GetAllNodesRecursive(start_node)

    def FindNodesByValue(self, val):
        nodes = self.GetAllNodes()
        return list(filter(lambda x: x.NodeValue == val, nodes))

    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        nodes = self.GetAllNodes()
        return len(list(filter(lambda x: x.Children == [], nodes)))
