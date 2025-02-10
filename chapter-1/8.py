def test_question():
  """
  Calculates the equivalent non-negative index value based on a negative index
  for all possible indexes of `l`.
  """
  test_count = 0
  l = [1, 2, 3, 4, 5]
  for k in range(-1, -(len(l) + 1), -1):
    j = len(l) - abs(k)
    assert(l[k] == l[j])
    test_count += 1
  assert(test_count == 5)