def minmax(data):
  """
  Returns the smallest and largest numbers in the form of a tuple (smallest, largest).
  """
  n_min, n_max = data[0], data[0]
  for i in range(1, len(data)):
    n = data[i]
    if n > n_max:
      n_max = n
    if n < n_min:
      n_min = n
  return n_min, n_max

def test_minmax():
  assert(minmax([0]) == (0, 0))
  assert(minmax([0, 0]) == (0, 0))
  assert(minmax([0, 1]) == (0, 1))
  assert(minmax([1, 2]) == (1, 2))
  assert(minmax([1, 2, 3, 4]) == (1, 4))
  assert(minmax([4, 3, 2, 1]) == (1, 4))
  assert(minmax([3, 1, 4, 2]) == (1, 4))
  assert(minmax([-1, -2, -3, -4]) == (-4, -1))
  assert(minmax([-4, -3, -2, -1]) == (-4, -1))
  assert(minmax([-3, -4, -1, -2]) == (-4, -1))