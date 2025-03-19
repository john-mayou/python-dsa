"""
Show that if p(n) is a polynomical in n, then log(p(n)) is O(log(n)):

The time complexity of p(n) is determined by its leading term a*n^k.
Taking the log log(a*n^k) we get:
  = log(a) + log(n^k)
  = log(a) + k*log(n)
  = k*log(n) (log(a) does not impact asymptotic growth)
  = log(n) (constants ommited in Big O)
"""