def count_two_divisions(n: int) -> int:  
  """
  Counts the number of divisions by 2 it takes for `n` to be less than 2.
  """
  
  if n < 2:
    return 0
  
  divisions = 0
  while (n >= 2):
    n /= 2
    divisions += 1
    
  return divisions

def test_count_divisions():
  assert(count_two_divisions(-1) == 0)
  assert(count_two_divisions(0) == 0)
  assert(count_two_divisions(1) == 0)
  assert(count_two_divisions(2) == 1)
  assert(count_two_divisions(3) == 1)
  assert(count_two_divisions(4) == 2)
  assert(count_two_divisions(5) == 2)
  assert(count_two_divisions(25) == 4)