def is_even(k: int) -> bool:
  """
  Determines if `k` is even without the use of:
  - Multiplication
  - Modulo
  - Division
  """
  even = True
  for i in range(abs(k)):
    even = not even
  return even

def test_is_even():
  assert(is_even(-2))
  assert(not is_even(-1))
  assert(is_even(0))
  assert(not is_even(1))
  assert(is_even(2))
  assert(not is_even(3))
  assert(is_even(4))
  assert(is_even(10))
  assert(not is_even(25))
