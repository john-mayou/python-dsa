def test_question():
  """
  Demonstrates catching an IndexError.
  """
  
  try:
    l = []
    l[0] = 1
  except IndexError:
    print("Don't try buffer overflow attack in Python!")