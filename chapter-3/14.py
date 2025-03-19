"""
Show that O(max{f(n),g(n)}) = O(f(n)+g(n)):

since either f(n) or will dominate:
  f(n)+g(n) <= 2(max{f(n),g(n)})
  f(n)+g(n) <= c(max{f(n),g(n)})
  
by definition of Big O:
  f(n)+g(n) is O(max{f(n),g(n)})
  
since max{f(n),g(n)} <= f(n) + g(n):
  max{f(n),g(n)} is O(f(n)+g(n))

both sides hold, thus O(max{f(n),g(n)}) = O(f(n)+g(n))
"""