def example2(S):
    n = len(S)
    total = 0
    for j in range(0, n, 2):
        total += S[j]
    return total

"""
Give the Big O, in terms of n, of the running time of the example2 function shown in
Code Fragmnent 3.10

The complexity is O(n)
"""