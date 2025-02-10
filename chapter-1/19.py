
ASCII_a = ord('a')

def test_question():
  """
  Demonstrates creating an alphabet list with list comprehension.
  """
  actual = [chr(ASCII_a + i) for i in range(26)]
  expected = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  assert(actual == expected)