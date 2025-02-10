def count_chars(s: str) -> int:
  """
  Counts the number of characters in a string.
  """
  count = 0
  for _ in s: count += 1
  return count

def test_count_chars():
  assert(count_chars('') == 0)
  assert(count_chars('a') == 1)
  assert(count_chars('aa') == 2)
  assert(count_chars('ab') == 2)
  assert(count_chars('abcd') == 4)
  assert(count_chars('dcba') == 4)
  assert(count_chars('a a') == 3)
  assert(count_chars('a-a') == 3)