from typing import Union

def dot_product(l1: list[int], l2: list[int]) -> Union[list[int], None]:
  """
  Returns the dot product of `l1` and `l2`.
  """
  if len(l1) != len(l2):
    return None
  dotp = []
  for i in range(len(l1)):
    dotp.append(l1[i] * l2[i])
  return dotp

def test_dot_product():
  assert(dot_product([], []) == [])
  assert(dot_product([], [1]) == None)
  assert(dot_product([1], []) == None)
  assert(dot_product([1], [1]) == [1])
  assert(dot_product([1, 1], [1, 1]) == [1, 1])
  assert(dot_product([1, 1], [2, 3]) == [2, 3])
  assert(dot_product([1, 2, 3], [3, 2, 1]) == [3, 4, 3])
  assert(dot_product([3, 2, 1], [1, 2, 3]) == [3, 4, 3])