def unique(S: list[int]) -> bool:
    """
    Time: O(n)
    Space: O(n)
    Recursive Depth: n
    """
    def unique_recurse(index: int, visited: set[int]) -> bool:
        if index >= len(S): return True
        if S[index] in visited: return False
        visited.add(S[index])
        return unique_recurse(index + 1, visited)
    return unique_recurse(0, set())

def test_unique():
    assert(unique([]))
    assert(unique([0]))
    assert(not unique([0, 0]))
    assert(unique([0, 1]))
    assert(unique([0, 1, 2]))
    assert(unique([0, 1, 2, 3]))
    assert(not unique([0, 1, 2, 2]))
    assert(not unique([2, 2, 1, 0]))
    assert(not unique([1, 2, 2, 0]))