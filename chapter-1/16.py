def scale(l: list[int], factor: int) -> list[int]:
  """
  Scales each value in `l` by `factor` and returns the list.
  """
  for i in range(len(l)):
    l[i] *= factor
  return l
  
def test_scale():
  assert(scale([], 2) == [])
  assert(scale([0], 2) == [0])
  assert(scale([1], 2) == [2])
  assert(scale([2], 2) == [4])
  assert(scale([2], 3) == [6])
  assert(scale([2], 4) == [8])
  assert(scale([0, 1, 2], 2) == [0, 2, 4])
  assert(scale([2, 1, 0], 2) == [4, 2, 0])