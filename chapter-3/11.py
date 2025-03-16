# Show that if d(n) is O(f(n)) and e(n) is O(g(n)), then d(n)+e(n) is O(f(n)+g(n))
#
# d(n) <= c1*f(n)
# e(n) <= c2*g(n)
#
# d(n)+e(n) <= c1*f(n)+c2*g(n)
# d(n)+e(n) <= c(f(n)+g(n))
# 
# By definition of Big O:
#   d(n)+e(n) is O(f(n)+g(n))