def test_question():
  """
  Demonstrates list comprehension syntax.
  """
  actual = [i*(i+1) for i in range(10)]
  expected = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
  assert(actual == expected)