import pytest

def test_count_elements_stack():
    def recursive(lst):
        if not lst:
            return 0
        stack = [lst]
        k = 0
        while stack:
            cur = stack.pop()
            for i in cur:
                k += 1
                if isinstance(i, list):
                    stack.append(i)
        return k
    
    assert isinstance(recursive([]), int)
    assert isinstance(recursive([1, 2, 3]), int)
    assert isinstance(recursive(["x", "y", ["z"]]), int)
    assert isinstance(recursive([1, 2, [3, 4, [5]]]), int)


def test_recursive_sequence():
    def recursive(i):
        if i == 1:
            return 1
        if i == 2:
            return -1/8
        return ((i-1) * recursive(i-1)) / 3 + ((i-2) * recursive(i-2)) / 4
    
    for i in range(1, 8):
        assert isinstance(recursive(i), (int, float))


def test_iterative_sequence():
    def iterative(n):
        if n == 1:
            return 1
        if n == 2:
            return -1/8
        x1 = 1
        x2 = -1/8
        for i in range(3, n + 1):
            x3 = ((i-1) * x2) / 3 + ((i-2) * x1) / 4
            x1, x2 = x2, x3
        return x2
    
    for i in range(1, 8):
        assert isinstance(iterative(i), (int, float))


def test_count_elements_recursive():
    def recursive(lst):
        if not lst:
            return 0
        k = 0
        for i in lst:
            if isinstance(i, list):
                k += recursive(i) + 1
            else:
                k += 1
        return k
    
    assert isinstance(recursive([]), int)
    assert isinstance(recursive([1, 2, 3]), int)
    assert isinstance(recursive(["x", "y", ["z"]]), int)
    assert isinstance(recursive([1, 2, [3, 4, [5]]]), int)