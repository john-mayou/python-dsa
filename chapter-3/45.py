def algo(S, n):
    expected_sum = (n*(n-1))/2
    actual_sum = sum(S)
    return expected_sum - actual_sum

def test_algo():
    assert(algo([0, 2, 6, 5, 4, 3], 7) == 1)