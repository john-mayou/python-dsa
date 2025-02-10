def remove_puncuation(s: str) -> str:
  return "".join([ch for ch in s if ch.isalnum() or ch.isspace()])

def test_remove_puncuation():
  assert(remove_puncuation('') == '')
  assert(remove_puncuation('a') == 'a')
  assert(remove_puncuation('1') == '1')
  assert(remove_puncuation(' ') == ' ')
  assert(remove_puncuation('-a') == 'a')
  assert(remove_puncuation('a-') == 'a')
  assert(remove_puncuation('a-a') == 'aa')
  assert(remove_puncuation("Let's try, Mike.") == 'Lets try Mike')