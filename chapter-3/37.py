"""
Give an example of a positive function f(n) such that f(n) is
neither O(n) nor (omega)(n):

f(n) = {
    n^2: if n is even
      1: if n is odd
}

since:
  n^2 cannot be upper bounded by O(n) when n is even
  there is no constant where c*n is the lower bounded of 1
"""