"""
Perform an experimental analysis of the three algorithms prefix average1,
prefix average2, and prefix average3, from Section 3.3.3. Visualize their
running times as a function of the input size with a log-log chart.
"""

def prefix_average1(S):
    """
    Runs in O(n^2)
    """
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += S[i]
        A[j] = total / (j+1)
    return A

def prefix_average2(S):
    """
    Runs in O(n^2)
    """
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j+1)
    return A

def prefix_average3(S):
    """
    Runs in O(n)
    """
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j+1)
    return A