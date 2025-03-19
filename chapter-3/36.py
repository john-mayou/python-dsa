def ten_largest(A):
    """
    Complexity is O(nlog(n))
    """
    return sorted(A)[-10:]

def test_ten_largest():
    assert(ten_largest([]) == [])
    assert(
        sorted(ten_largest([20, 15, 10, 5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30])) ==
        [10, 10, 11, 12, 13, 14, 15, 15, 20, 30]
    )