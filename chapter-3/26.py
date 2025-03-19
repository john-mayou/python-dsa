def example4(S):
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total

"""
Give the Big O, in terms of n, of the running time of the example4 function shown in
Code Fragmnent 3.10

The complexity is O(n)
"""