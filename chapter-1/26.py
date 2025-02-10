def arithmetic_test(a: int, b: int, c: int) -> bool:
  """
  Determines if `a`, `b`, and `c` can make a correct equation.
  """
  
  # addition
  if a+b==c or a+c==b or b+c==a:
    return True
  
  # subtraction
  if a-b==c or b-a==c or \
    a-c==b or c-a==b or \
    b-c==a or c-b==a:
      return True
  
  # multiplication
  if a*b==c or a*c==b or b*c==a:
    return True
  
  # division
  if (a != 0 and (c/a==b or b/a==c)) or \
    (b != 0 and (a/b==c or c/b==a)) or \
    (c != 0 and (a/c==b or b/c==a)):
      return True
  
  return False

def test_arithmetic_test():
  # addition
  assert(arithmetic_test(0, 0, 0))
  assert(arithmetic_test(1, 2, 3))
  assert(arithmetic_test(3, 2, 1))
  assert(arithmetic_test(1, 3, 2))
  
  # subtraction
  assert(arithmetic_test(0, 0, 0))
  assert(arithmetic_test(1, 2, 3))
  assert(arithmetic_test(3, 2, 1))
  assert(arithmetic_test(1, 3, 2))
  
  # multiplication
  assert(arithmetic_test(0, 0, 0))
  assert(arithmetic_test(2, 3, 6))
  assert(arithmetic_test(6, 3, 2))
  assert(arithmetic_test(2, 6, 3))

  # division
  assert(arithmetic_test(0, 0, 0))
  assert(arithmetic_test(2, 3, 6))
  assert(arithmetic_test(6, 3, 2))
  assert(arithmetic_test(2, 6, 3))
  
  # failures
  assert(not arithmetic_test(1, 9, 1))
  assert(not arithmetic_test(2, 8, 7))
  assert(not arithmetic_test(1, 4, 1))