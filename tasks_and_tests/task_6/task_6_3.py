from .task_6 import BalancedBST, BSTNode


def test_generate_tree():
    tree = BalancedBST()
    tree.GenerateTree([1, 2, 3, 4, 5, 6, 7])
    assert tree.Root.NodeKey == 4
    assert tree.Root.LeftChild.NodeKey == 2
    assert tree.Root.RightChild.NodeKey == 6
    assert tree.Root.LeftChild.LeftChild.NodeKey == 1
    assert tree.Root.LeftChild.RightChild.NodeKey == 3
    assert tree.Root.RightChild.LeftChild.NodeKey == 5
    assert tree.Root.RightChild.RightChild.NodeKey == 7

    assert tree.Root.Level == 0
    assert tree.Root.LeftChild.Level == 1
    assert tree.Root.RightChild.Level == 1
    assert tree.Root.LeftChild.LeftChild.Level == 2
    assert tree.Root.LeftChild.RightChild.Level == 2
    assert tree.Root.RightChild.LeftChild.Level == 2
    assert tree.Root.RightChild.RightChild.Level == 2


def test_is_balanced():
    tree = BalancedBST()
    tree.GenerateTree([4, 2, 6, 1])
    assert tree.IsBalanced(tree.Root)
    assert tree.IsBalanced(tree.Root.LeftChild)
    assert tree.IsBalanced(tree.Root.RightChild)

    tree.Root.LeftChild.LeftChild.RightChild = BSTNode(0, tree.Root.LeftChild.LeftChild)
    assert not tree.IsBalanced(tree.Root)
    assert not tree.IsBalanced(tree.Root.LeftChild)
    assert tree.IsBalanced(tree.Root.RightChild)
    assert tree.IsBalanced(tree.Root.LeftChild.LeftChild)
