def distinct(l: list[int]) -> bool:
  """
  Determines if all values of the list are different from each other.
  """
  if len(l) <= 1:
    return True
  s = set()
  for n in l:
    if n in s:
      return False
    s.add(n)
  return True

def test_distinct():
  assert(distinct([]))
  assert(distinct([0]))
  assert(distinct([0, 1]))
  assert(not distinct([0, 0]))
  assert(not distinct([0, 1, 0]))
  assert(distinct([0, 1, 2, 3]))
  assert(distinct([3, 2, 1, 0]))
  assert(not distinct([1, 0, 0, 2]))