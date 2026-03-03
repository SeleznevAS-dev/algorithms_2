from .task_1 import SimpleTreeNode, SimpleTree


def test_AddChild():
    node = SimpleTreeNode(1, None)
    tree = SimpleTree(node)
    child_node = SimpleTreeNode(2, None)
    tree.AddChild(node, child_node)
    assert child_node in node.Children
    assert child_node.Parent == node


def test_DeleteNode():
    node = SimpleTreeNode(1, None)
    tree = SimpleTree(node)
    child_node = SimpleTreeNode(2, None)
    tree.AddChild(node, child_node)
    tree.DeleteNode(child_node)
    assert child_node not in node.Children
    assert child_node.Parent is None


def test_GetAllNodes():
    node = SimpleTreeNode(1, None)
    tree = SimpleTree(node)
    child_node1 = SimpleTreeNode(2, None)
    child_node2 = SimpleTreeNode(3, None)
    tree.AddChild(node, child_node1)
    tree.AddChild(node, child_node2)
    all_nodes = tree.GetAllNodes()
    assert node in all_nodes
    assert child_node1 in all_nodes
    assert child_node2 in all_nodes


def test_FindNodesByValue():
    node = SimpleTreeNode(1, None)
    tree = SimpleTree(node)
    child_node1 = SimpleTreeNode(2, None)
    child_node2 = SimpleTreeNode(2, None)
    tree.AddChild(node, child_node1)
    tree.AddChild(node, child_node2)
    found_nodes = tree.FindNodesByValue(2)
    assert child_node1 in found_nodes
    assert child_node2 in found_nodes


def test_MoveNode():
    node = SimpleTreeNode(1, None)
    tree = SimpleTree(node)
    child_node1 = SimpleTreeNode(2, None)
    child_node2 = SimpleTreeNode(3, None)
    tree.AddChild(node, child_node1)
    tree.AddChild(node, child_node2)
    tree.MoveNode(child_node1, child_node2)
    assert child_node1 in child_node2.Children
    assert child_node1.Parent == child_node2


def test_Count():
    node = SimpleTreeNode(1, None)
    tree = SimpleTree(node)
    child_node1 = SimpleTreeNode(2, None)
    child_node2 = SimpleTreeNode(3, None)
    tree.AddChild(node, child_node1)
    tree.AddChild(node, child_node2)
    assert tree.Count() == 3


def test_LeafCount():
    node = SimpleTreeNode(1, None)
    tree = SimpleTree(node)
    child_node1 = SimpleTreeNode(2, None)
    child_node2 = SimpleTreeNode(3, None)
    tree.AddChild(node, child_node1)
    tree.AddChild(node, child_node2)
    assert tree.LeafCount() == 2
