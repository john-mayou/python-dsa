"""
Perform experimental analysis to test the hypothesis that Python's sorted
method runs in O(nlog(n)) time on average.
"""

import timeit
import random
import math

def measure_sort_time(n):
    data = [random.randint(0, 10**6) for _ in range(n)]
    start_time = timeit.default_timer()
    sorted(data)
    return timeit.default_timer() - start_time

sizes = [2**i for i in range(10, 20)]
times = [measure_sort_time(n) for n in sizes]

nlogn = [n*math.log2(n) for n in sizes]
nlogn = [t / nlogn[-1] * times[-1] for t in nlogn] # normalize

for i in range(len(sizes)):
    print(f"size={sizes[i]}; time={times[i]} nlogn={nlogn[i]}")