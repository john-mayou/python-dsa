"""
Show that 2^(n+1) is O(2^n):

2^(n+1) = 2*2^n
2^(n+1) <= 2*2^n

since the inequality holds for c = 2 and n >= 1, by definition of Big O:
  2^(n+1) is O(2^n)
"""