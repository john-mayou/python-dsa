def disjointness(A, B, C):
    """
    Complexity is O(nlog(n))
    """

    pA, pB, pC = 0, 0, 0
    A, B, C = sorted(A), sorted(B), sorted(C)
    lenA, lenB, lenC = len(A), len(B), len(C)
    
    while pA < lenA and pB < lenB and pC < lenC:
        a, b, c = A[pA], B[pB], C[pC]
        
        if a == b == c:
            return False
        
        m = min(a, b, c)

        if a == m: pA += 1
        if b == m: pB += 1
        if c == m: pC += 1
    
    return True

def test_disjointness():
    A1 = [1, 2, 3]
    B1 = [4, 5, 6]
    C1 = [7, 8, 9]
    assert(disjointness(A1, B1, C1))
    
    A1 = [1, 2, 3, 7]
    B1 = [4, 5, 6]
    C1 = [7, 8, 9]
    assert(disjointness(A1, B1, C1))
    
    A3 = [1, 2, 3, 7]
    B3 = [4, 5, 7]
    C3 = [6, 7, 8]
    assert(not disjointness(A3, B3, C3))