from .task_9 import SimpleTree, SimpleTreeNode


def test_even_trees():
    simple_tree = SimpleTree(SimpleTreeNode(1, None))
    node2 = SimpleTreeNode(2, None)
    simple_tree.AddChild(simple_tree.Root, node2)
    node3 = SimpleTreeNode(3, None)
    simple_tree.AddChild(simple_tree.Root, node3)
    node6 = SimpleTreeNode(6, None)
    simple_tree.AddChild(simple_tree.Root, node6)
    node5 = SimpleTreeNode(5, None)
    simple_tree.AddChild(node2, node5)
    node7 = SimpleTreeNode(7, None)
    simple_tree.AddChild(node2, node7)
    node4 = SimpleTreeNode(4, None)
    simple_tree.AddChild(node3, node4)
    node8 = SimpleTreeNode(8, None)
    simple_tree.AddChild(node6, node8)
    node9 = SimpleTreeNode(9, None)
    simple_tree.AddChild(node8, node9)
    node10 = SimpleTreeNode(10, None)
    simple_tree.AddChild(node8, node10)

    result = simple_tree.EvenTrees()
    assert result == [simple_tree.Root, node3, simple_tree.Root, node6]
