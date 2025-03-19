"""
Show that (n+1)^5 is O(n^5):

expand:
  (n+1)^5 = n^5 + 5n^4 + 10n^3 + 10n^2 + 5n + 1
  
n^5 will dominate at large n values, thus:
  (n+1)^5 is O(n^5)
"""