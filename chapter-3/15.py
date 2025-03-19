"""
Show that f(n) is O(g(n)) if and only if g(n) is (omega)(f(n)):

f(n) is O(g(n)) meaning:
  f(n) <= c*g(n)
  (1/c)*f(n) <= g(n)
  
  by definition of Big Omega:
    g(n) is (omega)(f(n))
  
g(n) is (omega)(f(n)) meaning:
  g(n) >= c*f(n)
  (1/c)*g(n) >= f(n)
  
  by definition of Big O:
    f(n) is O(g(n))

both sides hold.
"""