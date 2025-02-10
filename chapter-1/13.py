def reverse2(l):
  """
  Reverses the values of the list in place and returns the list.
  """
  if len(l) <= 1:
    return l
  p1 = 0
  p2 = len(l) - 1
  while (p1 < p2):
    l[p1], l[p2] = l[p2], l[p1]
    p1 += 1
    p2 -= 1
  return l

def test_reverse2():
  assert(reverse2([]) == [])
  assert(reverse2([0]) == [0])
  assert(reverse2([0, 1]) == [1, 0])
  assert(reverse2([1, 0]) == [0, 1])
  assert(reverse2([1, 2, 3]) == [3, 2, 1])
  assert(reverse2([1, 2, 3, 4]) == [4, 3, 2, 1])
  assert(reverse2([4, 3, 2, 1]) == [1, 2, 3, 4])