# reverse([4, 3, 6, 2, 6], 0, 5)
# reverse([6, 3, 6, 2, 4], 1, 4)
# reverse([4, 2, 6, 3, 6], 2, 3)

def reverse(S):
    """
    Time -> O(n)
    Space -> O(n)
    """
    def reverse_helper(start, stop):
        if start < stop - 1:
            S[start], S[stop - 1] = S[stop - 1], S[start]
            reverse_helper(start + 1, stop - 1)
            
    reverse_helper(0, len(S))
            
    return S

def reverse2(S):
    """
    Time -> O(n)
    Space -> O(1)
    """
    left, right = 0, len(S)-1
    while left < right:
        S[left], S[right] = S[right], S[left]
        left += 1
        right -= 1
    return S
        
def test_reverse():
    assert(reverse([]) == [])
    assert(reverse([0]) == [0])
    assert(reverse([0, 1]) == [1, 0])
    assert(reverse([1, 0]) == [0, 1])
    assert(reverse([1, 2, 3]) == [3, 2, 1])
    assert(reverse([3, 2, 1]) == [1, 2, 3])
    assert(reverse([5, 7, 9, 2]) == [2, 9, 7, 5])

def test_reverse2():
    assert(reverse2([]) == [])
    assert(reverse2([0]) == [0])
    assert(reverse2([0, 1]) == [1, 0])
    assert(reverse2([1, 0]) == [0, 1])
    assert(reverse2([1, 2, 3]) == [3, 2, 1])
    assert(reverse2([3, 2, 1]) == [1, 2, 3])
    assert(reverse2([5, 7, 9, 2]) == [2, 9, 7, 5])