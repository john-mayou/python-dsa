def product(x: int, y: int) -> int:
    """
    Time: O(y)
    Space: O(y)
    Recursive Depth: y
    """
    def resursively_add(x, y, total):
        if y == 0: return total
        total += x
        y -= 1
        return resursively_add(x, y, total)
    return resursively_add(x, y, 0)

def test_product():
    assert(product(0, 0) == 0)
    assert(product(0, 1) == 0)
    assert(product(1, 1) == 1)
    assert(product(1, 2) == 2)
    assert(product(2, 2) == 4)
    assert(product(10, 10) == 100)