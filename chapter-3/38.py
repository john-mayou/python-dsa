"""
Show that (sigma)(n)(i=1) i^2 is O(n^3):

summation power sum formula:
  Sn = n(n+1)(2n+1)/6
  
= (n^2+n)(2n+1)/6
= (2n^3+n^2+2n^2+n)/6
= (1/3)n^3 - n^3 term dominates
= O(n^3) - constant is dropped
"""