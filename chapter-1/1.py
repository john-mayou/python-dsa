def is_multiple(n: int, m: int) -> bool:
  """
  Determines if `n` is a multiple of `m`.
  """
  if n == 0:
    return False
  return m % n == 0
  
def test_is_multiple():
  assert(not is_multiple(0, 0))
  assert(is_multiple(1, 1))
  assert(is_multiple(2, 2))
  assert(is_multiple(2, 4))
  assert(is_multiple(2, 6))
  assert(not is_multiple(5, 24))
  assert(is_multiple(5, 25))
  assert(not is_multiple(5, 26))