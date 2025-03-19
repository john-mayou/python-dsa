"""
Describe an algorithm for finding both the minimum and maximum of n
numbers using fewer than 3n/2 comparisons:
"""

def algorithm(N):
    """
    Complexity is O(n) and uses ~ 3n/2 comparisons.
    """
    if len(N) == 0:
        return [None, None]
    if len(N) == 1:
        return [N[0], N[0]]
    
    if N[0] < N[1]:
        min_v = N[0]
        max_v = N[1]
    else:
        min_v = N[1]
        max_v = N[0]
        
    for i in range(2, len(N) - 1, 2):
        if (N[i] < N[i+1]):
            min_v = min(N[i], min_v)
            max_v = max(N[i+1], max_v)
        else:
            min_v = min(N[i+1], min_v)
            max_v = max(N[i], max_v)
    
    if len(N) % 2 == 1:
        min_v = min(N[len(N) - 1], min_v)
        max_v = max(N[len(N) - 1], max_v)

    return [min_v, max_v]

def test_algorith():
    assert(algorithm([]) == [None, None])
    assert(algorithm([1]) == [1, 1])
    assert(algorithm([1, 2]) == [1, 2])
    assert(algorithm([2, 1]) == [1, 2])
    assert(algorithm([1, 2, 3, 4]) == [1, 4])
    assert(algorithm([4, 3, 2, 1]) == [1, 4])