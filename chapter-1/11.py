def test_question():
  """
  This demostrates how to use list comprehension syntax.
  """
  actual = [2**i for i in range(0, 9)]
  expected = [1, 2, 4, 8, 16, 32, 64, 128, 256]
  assert actual == expected