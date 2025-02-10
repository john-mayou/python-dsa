def test_question():
  """
  This demonstrates using the range function to interate through positive and
  negative values.
  """
  values = []
  for val in range(8, -9, -2):
    values.append(val)
  assert(values == [8, 6, 4, 2, 0, -2, -4, -6, -8])