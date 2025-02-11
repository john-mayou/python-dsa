import math

def pnorm(v: list[int], p: int = 2) -> int:
  """
  Finds the p-norm of a vector in n-dimensional space.
  """
  return math.sqrt(sum([n**p for n in v]))

def test_pnorm():
  assert(pnorm([]) == 0)
  assert(pnorm([-2, -1, 0, 1, 2], 1) == 0)
  assert(pnorm([-2, -1, 0, 1, 2], 2) == math.sqrt(10)) # euclidean
  assert(pnorm([-2, -1, 0, 1, 2], 3) == 0)
  assert(pnorm([-2, -1, 0, 1, 2], 4) == math.sqrt(34))
  assert(pnorm([-2, -1, 0, 1, 2], 5) == 0)
  
  # real world
  assert(pnorm([4, 3]) == 5)