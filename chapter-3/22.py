"""
Show that ceil(f(n)) is O(f(n)), if f(n) is a positive nondecreasing function that
if always greater than 1:

since ceil will only ever increase the end value by 1, it does not affect the time complexity
given that there exists a constant c (e.g., 2) where ceil(f(n)) <= c*f(n) that holds for n >= 1
"""