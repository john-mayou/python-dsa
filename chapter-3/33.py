"""
Al and Bob are arguing about their algorithms. Al claims his O(nlog(n))-
time method is always faster than Bob's O(n2)-time method. To settle the
issue, they perform a set of experiments. To Al's dismay, they find that if
n < 100, the O(n2)-time algorithm runs faster, and only when n ≥ 100 is
the O(nlog(n))-time one better. Explain how this is possible.

Big O is meant for asymptotic growth rates where values of n are large.
Constants and lower order factors may influence the performance for small n.
For example, 100nlog(n) would run slower than 0.1n^2 for small values of n,
but would flip for large values of n.
"""