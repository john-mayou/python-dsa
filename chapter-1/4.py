def square_sum(n: int) -> int:
  """
  Returns the sum of squares for all positive integers less than `n`.
  """
  if n < 2:
    return 0
  total = 0
  for i in range(1, n):
    total += i**2
  return total

def test_square_sum():
  assert(square_sum(-1) == 0)
  assert(square_sum(0) == 0)
  assert(square_sum(1) == 0)
  assert(square_sum(2) == 1)
  assert(square_sum(3) == 5)
  assert(square_sum(4) == 14)
  assert(square_sum(10) == 285)