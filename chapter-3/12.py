# Show that if d(n) is O(f(n)) and e(n) is O(g(n)), then d(n)-e(n) is not
# necessarily O(f(n)-g(n)):
#
# Since Big O defines an upper bound, we can have time complexity of:
# 
# d(n) complexity = n^2 + n
# e(n) complexity = n^2
#
# d(n) is O(n^2)
# e(n) is O(n^2)
#
# In this scenario, O(f(n)-g(n)) would be:
#   O(0) (which is not a meaningful bound)
# 
# although the actual complexity would be:
#   n^2 + n - n^2 = n = O(n)
#
# O(0) != O(n), thus we cannot rely on d(n)-e(n) being O(f(n) - g(n))