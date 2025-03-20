"""
A sequence S contains n integers taken from the interval [0,4n], with repe-
titions allowed. Describe an efficient algorithm for determining an integer
value k that occurs the most often in S. What is the running time of your
algorithm?
"""

from collections import Counter

def algo(S):
    """
    Complexity is O(n)
    """
    if len(S) == 0: return None
    return max(Counter(S).items(), key=lambda x: x[1])[0]

def test_algo():
    assert(algo([]) == None)
    assert(algo([1]) == 1)
    assert(algo([1, 2, 3, 1, 2, 1, 1]) == 1)