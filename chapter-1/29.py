def str_possibilities(chars):
  """
  Finds all the possible string combinations from the given characters, where each
  character can only be used once.
  """
  
  if len(chars) <= 1:
    return chars
  
  possibilities = []
  
  def recurse(s, rest_chars):
    if len(rest_chars) == 1:
      possibilities.append(s + rest_chars[0])
    for i in range(len(rest_chars)):
      recurse(s + rest_chars[i], rest_chars[0:i] + rest_chars[i+1:])
  
  for i in range(len(chars)):
    recurse(chars[i], chars[0:i] + chars[i+1:])
    
  return possibilities

def test_possibilities():
  # unit
  assert(str_possibilities([]) == [])
  assert(str_possibilities(['a']) == ['a'])
  assert(sorted(str_possibilities(['a', 'b'])) == ['ab', 'ba'])
  
  # acceptance
  assert(len(str_possibilities(['a', 'c', 'd', 'g', 'o', 't'])) == 720)