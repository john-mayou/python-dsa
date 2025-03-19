def example1(S):
    n = len(S)
    total = 0
    for j in range(n):
        total += S[j]
    return total

"""
Give the Big O, in terms of n, of the running time of the example1 function shown in
Code Fragmnent 3.10

The complexity is O(n)
"""