from .task_4 import aBST


def test_aBST_depth_0():
    tree = aBST(0)
    assert tree.FindKeyIndex(25) == 0
    assert tree.FindKeyIndex(75) == 0
    assert tree.AddKey(50) == 0
    assert tree.AddKey(50) == 0
    assert tree.AddKey(25) == -1
    assert tree.AddKey(75) == -1

    assert tree.FindKeyIndex(50) == 0
    assert tree.FindKeyIndex(25) is None
    assert tree.FindKeyIndex(75) is None


def test_aBST_depth_1():
    tree = aBST(1)
    assert tree.AddKey(50) == 0
    assert tree.FindKeyIndex(25) == -1
    assert tree.FindKeyIndex(75) == -2
    assert tree.AddKey(25) == 1
    assert tree.AddKey(75) == 2

    assert tree.FindKeyIndex(50) == 0
    assert tree.FindKeyIndex(25) == 1
    assert tree.FindKeyIndex(75) == 2
    assert tree.FindKeyIndex(1) is None


def test_aBST_depth_3():
    tree = aBST(3)
    assert tree.AddKey(50) == 0
    assert tree.AddKey(25) == 1
    assert tree.AddKey(75) == 2
    assert tree.AddKey(12) == 3
    assert tree.AddKey(37) == 4
    assert tree.AddKey(62) == 5
    assert tree.AddKey(84) == 6
    assert tree.AddKey(6) == 7
    assert tree.AddKey(18) == 8
    assert tree.AddKey(31) == 9
    assert tree.AddKey(43) == 10
    assert tree.AddKey(55) == 11
    assert tree.AddKey(68) == 12
    assert tree.AddKey(79) == 13
    assert tree.AddKey(92) == 14

    assert tree.AddKey(100) == -1
    assert tree.AddKey(50) == 0
    assert tree.AddKey(5) == -1

    assert tree.FindKeyIndex(50) == 0
    assert tree.FindKeyIndex(25) == 1
    assert tree.FindKeyIndex(75) == 2
    assert tree.FindKeyIndex(1) is None


def test_aBST_wide_all_nodes():
    tree = aBST(3)
    assert tree.AddKey(50) == 0
    assert tree.AddKey(25) == 1
    assert tree.AddKey(75) == 2
    assert tree.AddKey(12) == 3
    assert tree.AddKey(37) == 4
    assert tree.AddKey(62) == 5
    assert tree.AddKey(84) == 6
    assert tree.AddKey(6) == 7
    assert tree.AddKey(18) == 8
    assert tree.AddKey(31) == 9
    assert tree.AddKey(43) == 10
    assert tree.AddKey(55) == 11
    assert tree.AddKey(68) == 12
    assert tree.AddKey(79) == 13
    assert tree.AddKey(92) == 14

    wide_all_nodes = tree.WideAllNodes()
    assert wide_all_nodes[0][0] == 50
    assert wide_all_nodes[1][0] == 25
    assert wide_all_nodes[1][1] == 75
    assert wide_all_nodes[2][0] == 12
    assert wide_all_nodes[2][1] == 37
    assert wide_all_nodes[2][2] == 62
    assert wide_all_nodes[2][3] == 84
    assert wide_all_nodes[3][0] == 6
    assert wide_all_nodes[3][1] == 18
    assert wide_all_nodes[3][2] == 31
    assert wide_all_nodes[3][3] == 43
    assert wide_all_nodes[3][4] == 55
    assert wide_all_nodes[3][5] == 68
    assert wide_all_nodes[3][6] == 79
    assert wide_all_nodes[3][7] == 92
