def distinct_pair(l: list[int]) -> bool:
  """
  Determines if there is a distinct pair of numbers whose product is odd.
  """
  odds = 0
  for n in l:
    if n % 2 == 1:
      odds += 1
      if odds == 2:
        return True
  return False

def test_distinct_pair():
  assert(distinct_pair([]) == False)
  assert(distinct_pair([0]) == False)
  assert(distinct_pair([0, 1]) == False)
  assert(distinct_pair([0, 1, 2]) == False)
  assert(distinct_pair([0, 1, 2, 3]) == True)
  assert(distinct_pair([1, 1]) == True)
  assert(distinct_pair([1, 2]) == False)
  assert(distinct_pair([2, 2]) == False)