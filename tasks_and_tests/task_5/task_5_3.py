from .task_5 import GenerateBBSTArray


def test_generate_bbst_array():
    assert GenerateBBSTArray([1, 2, 3, 4, 5, 6, 7]) == [4, 2, 6, 1, 3, 5, 7]

    assert GenerateBBSTArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [
        8,
        4,
        12,
        2,
        6,
        10,
        14,
        1,
        3,
        5,
        7,
        9,
        11,
        13,
        15,
    ]
