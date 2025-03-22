def log2int(n):
    """
    Time: O(log(n))
    Space: O(log(n))
    Recursive Depth: log(n)
    """
    def log2intdepth(_n, depth):
        if _n <= 1: return depth
        return log2intdepth(_n // 2, depth + 1)
    return log2intdepth(n, 0)

def log2int2(n):
    """
    Time: O(log(n))
    Space: O(1)
    """
    depth = 0
    while n > 1:
        n //= 2
        depth += 1
    return depth

def test_log2int():
    assert(log2int(0) == 0)
    assert(log2int(1) == 0)
    assert(log2int(2) == 1)
    assert(log2int(3) == 1)
    assert(log2int(4) == 2)
    
def test_log2int2():
    assert(log2int2(0) == 0)
    assert(log2int2(1) == 0)
    assert(log2int2(2) == 1)
    assert(log2int2(3) == 1)
    assert(log2int2(4) == 2)