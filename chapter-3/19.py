"""
Show that n is O(n*log(n)):

n <= c*n*log(n)
1 <= c*log(n)

this inequality holds for c = 1 and n >= 2, thus by definition of Big O:
  n is O(n*log(n)) although a tigher upper bound complexity would be O(n)
"""