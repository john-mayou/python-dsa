def find(S):
    """
    Recursive Depth: n
    Time: O(n)
    Space: O(n)
    """
    if len(S) == 0: return [None, None]
    
    def find_recursively(curr_min, curr_max, curr_i):
        if curr_i >= len(S): return [curr_min, curr_max]
        return find_recursively(
            min(curr_min, S[curr_i]),
            max(curr_max, S[curr_i]),
            curr_i + 1
        )
        
    return find_recursively(S[0], S[0], 1)

def test_find():
    assert(find([]) == [None, None])
    assert(find([0]) == [0, 0])
    assert(find([0, 1]) == [0, 1])
    assert(find([1, 0]) == [0, 1])
    assert(find([1, 2, 3]) == [1, 3])
    assert(find([3, 2, 1]) == [1, 3])
    assert(find([3, 4, 1, 2]) == [1, 4])
