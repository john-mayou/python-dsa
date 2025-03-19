def example3(S):
    n = len(S)
    total = 0
    for j in range(n):
        for k in range(1+j):
            total += S[k]
    return total

"""
Give the Big O, in terms of n, of the running time of the example3 function shown in
Code Fragmnent 3.10

The complexity is O(n^2)
"""