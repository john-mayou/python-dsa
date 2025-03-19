def example5(A, B):
    n = len(A)
    count = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1+j):
                total += A[k]
        if B[i] == total:
            count += 1
    return count

"""
Give the Big O, in terms of n, of the running time of the example5 function shown in
Code Fragmnent 3.10

The complexity is O(n^3)
"""