from .task_7 import Heap


def test_make_heap():
    heap = Heap()
    heap.MakeHeap([1, 2, 3, 4, 5, 6, 7], 2)
    assert heap.HeapArray == [7, 4, 6, 1, 3, 2, 5]


def test_get_max():
    heap = Heap()
    heap.MakeHeap([1, 2, 3, 4, 5, 6, 7], 2)
    assert heap.HeapArray[0] == 7
    assert heap.GetMax() == 7
    assert heap.HeapArray[0] == 6
    assert heap.GetMax() == 6
    assert heap.HeapArray[0] == 5
    assert heap.GetMax() == 5
    assert heap.HeapArray[0] == 4
    assert heap.GetMax() == 4
    assert heap.HeapArray[0] == 3
    assert heap.GetMax() == 3
    assert heap.HeapArray[0] == 2
    assert heap.GetMax() == 2
    assert heap.HeapArray[0] == 1
    assert heap.GetMax() == 1
    assert heap.HeapArray[0] is None
    assert heap.GetMax() == -1


def test_add():
    heap = Heap()
    heap.MakeHeap([1, 2, 3, 4, 5], 2)
    assert heap.Add(7) is True
    assert heap.HeapArray[0] == 7
    assert heap.Add(6) is True
    assert heap.HeapArray[0] == 7
    assert heap.Add(8) is False


def test_is_heap_correct():
    heap = Heap()
    heap.MakeHeap([1, 2, 3, 4, 5, 6, 7], 2)
    assert heap.HeapArray == [7, 4, 6, 1, 3, 2, 5]

    heap.GetMax()
    assert heap.HeapArray == [6, 4, 5, 1, 3, 2, None]
    heap.GetMax()
    assert heap.HeapArray == [5, 4, 2, 1, 3, None, None]
    heap.GetMax()
    assert heap.HeapArray == [4, 3, 2, 1, None, None, None]
    heap.Add(7)
    assert heap.HeapArray == [7, 4, 2, 1, 3, None, None]
    heap.Add(6)
    assert heap.HeapArray == [7, 4, 6, 1, 3, 2, None]
    heap.Add(5)
    assert heap.HeapArray == [7, 4, 6, 1, 3, 2, 5]
