"""
Show that logb(f(n)) is (theta)(log(f(n))) if b > 1 is a constant:

logb(f(n)
= log(f(n))/log(b)
= (1/log(b))*log(f(n))

so:
  (c1/log(b))*log(f(n)) <= logb(f(n)) <= (c2/log(b))*log(f(n))
  where: c1=1, c2=2

thus:
  logb(f(n)) is (theta)(log(f(n)))
"""