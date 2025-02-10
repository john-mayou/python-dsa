def odd_square_sum(n: int) -> int:
  """
  Returns the sum of all odd positive integer squares for numbers less than `n`.
  """
  if n < 2:
    return 0
  return sum([i**2 for i in range(1, n, 2) if i % 2 == 1])

def test_odd_square_sum():
  assert(odd_square_sum(-1) == 0)
  assert(odd_square_sum(0) == 0)
  assert(odd_square_sum(1) == 0)
  assert(odd_square_sum(2) == 1)
  assert(odd_square_sum(3) == 1)
  assert(odd_square_sum(4) == 10)
  assert(odd_square_sum(5) == 10)
  assert(odd_square_sum(10) == 165)