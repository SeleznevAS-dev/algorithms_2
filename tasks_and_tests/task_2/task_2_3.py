from .task_2 import BST, BSTNode


def test_find():
    bst = BST(BSTNode(8, 8, None))
    assert (
        bst.FindNodeByKey(4).NodeHasKey is False and bst.FindNodeByKey(4).ToLeft is True
    )
    assert (
        bst.FindNodeByKey(12).NodeHasKey is False
        and bst.FindNodeByKey(12).ToLeft is False
    )
    assert bst.FindNodeByKey(8).NodeHasKey is True


def test_add():
    bst = BST(BSTNode(8, 8, None))
    assert (
        bst.FindNodeByKey(4).NodeHasKey is False and bst.FindNodeByKey(4).ToLeft is True
    )
    assert bst.AddKeyValue(4, 4) is True
    assert bst.FindNodeByKey(4).NodeHasKey is True
    assert (
        bst.FindNodeByKey(12).NodeHasKey is False
        and bst.FindNodeByKey(12).ToLeft is False
    )
    assert bst.AddKeyValue(12, 12) is True
    assert bst.FindNodeByKey(12).NodeHasKey is True
    assert bst.AddKeyValue(8, 8) is False


def test_find_min_max():
    node_root = BSTNode(8, 8, None)
    bst = BST(node_root)
    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    assert bst.FinMinMax(node_root, False).NodeKey == 4
    assert bst.FinMinMax(node_root, True).NodeKey == 12

    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)
    bst.AddKeyValue(10, 10)

    assert node_root.LeftChild and bst.FinMinMax(node_root.LeftChild, True).NodeKey == 6
    assert (
        node_root.RightChild
        and bst.FinMinMax(node_root.RightChild, False).NodeKey == 10
    )


def test_delete_node():
    node_root = BSTNode(8, 8, None)
    bst = BST(node_root)
    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)

    assert bst.FindNodeByKey(2).NodeHasKey is True
    assert bst.DeleteNodeByKey(2) is True
    assert bst.FindNodeByKey(2).NodeHasKey is False

    assert bst.FindNodeByKey(4).NodeHasKey is True
    assert bst.DeleteNodeByKey(4) is True
    assert bst.FindNodeByKey(4).NodeHasKey is False
    assert bst.FindNodeByKey(6).NodeHasKey is True

    assert bst.FindNodeByKey(8).NodeHasKey is True
    assert bst.DeleteNodeByKey(8) is True
    assert bst.FindNodeByKey(8).NodeHasKey is False
    assert bst.FindNodeByKey(6).NodeHasKey is True
    assert bst.FindNodeByKey(12).NodeHasKey is True
    assert bst.Root and bst.Root.NodeKey == 12
    assert bst.Root and bst.Root.LeftChild and bst.Root.LeftChild.NodeKey == 6


def test_count():
    node_root = BSTNode(8, 8, None)
    bst = BST(node_root)
    assert bst.Count() == 1
    bst.AddKeyValue(4, 4)
    assert bst.Count() == 2
    bst.AddKeyValue(12, 12)
    assert bst.Count() == 3
    bst.AddKeyValue(2, 2)
    assert bst.Count() == 4
    bst.AddKeyValue(6, 6)
    assert bst.Count() == 5
    bst.AddKeyValue(10, 10)
    assert bst.Count() == 6
    bst.AddKeyValue(14, 14)
    assert bst.Count() == 7
    bst.AddKeyValue(1, 1)
    assert bst.Count() == 8
    bst.AddKeyValue(3, 3)
    assert bst.Count() == 9
    bst.AddKeyValue(5, 5)
    assert bst.Count() == 10
    bst.AddKeyValue(7, 7)
    assert bst.Count() == 11
    bst.AddKeyValue(9, 9)
    assert bst.Count() == 12
    bst.AddKeyValue(11, 11)
    assert bst.Count() == 13
    bst.AddKeyValue(13, 13)
    assert bst.Count() == 14
    bst.AddKeyValue(15, 15)
    assert bst.Count() == 15
