from .task_3 import BST, BSTNode


def test_wide_all_nodes():
    node_root = BSTNode(8, 8, None)
    bst = BST(node_root)
    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)

    all_nodes = bst.WideAllNodes()
    assert all_nodes[0].NodeKey == 8
    assert all_nodes[1].NodeKey == 4
    assert all_nodes[2].NodeKey == 12
    assert all_nodes[3].NodeKey == 2
    assert all_nodes[4].NodeKey == 6

def test_deep_all_nodes():
    node_root = BSTNode(8, 8, None)
    bst = BST(node_root)
    bst.AddKeyValue(4, 4)
    bst.AddKeyValue(12, 12)
    bst.AddKeyValue(2, 2)
    bst.AddKeyValue(6, 6)

    all_nodes = bst.DeepAllNodes(0)
    assert all_nodes[0].NodeKey == 2
    assert all_nodes[1].NodeKey == 4
    assert all_nodes[2].NodeKey == 6
    assert all_nodes[3].NodeKey == 8
    assert all_nodes[4].NodeKey == 12
    
    all_nodes = bst.DeepAllNodes(1)
    assert all_nodes[0].NodeKey == 2
    assert all_nodes[1].NodeKey == 6
    assert all_nodes[2].NodeKey == 4
    assert all_nodes[3].NodeKey == 12
    assert all_nodes[4].NodeKey == 8
    
    all_nodes = bst.DeepAllNodes(2)
    assert all_nodes[0].NodeKey == 8
    assert all_nodes[1].NodeKey == 4
    assert all_nodes[2].NodeKey == 2
    assert all_nodes[3].NodeKey == 6
    assert all_nodes[4].NodeKey == 12
    