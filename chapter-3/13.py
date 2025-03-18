"""
Show that if d(n) is (O(f(n))) and f(n) is O(g(n)), then d(n) is O(g(n)):

d(n) <= c1*f(n)
f(n) <= c2*g(n)

substitute f(n):
  d(n) <= c1*c2*g(n)

since c1*c2 is just another constant:
  d(n) <= c*g(n)
  
by the definition of Big O:
  d(n) is O(g(n))
"""