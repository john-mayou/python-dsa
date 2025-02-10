def test_question():
  """
  This demonstrates using the range step argument.
  """
  values = []
  for val in range(50, 81, 10):
    values.append(val)
  assert(values == [50, 60, 70, 80])