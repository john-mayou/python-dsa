def word_occurance(sentence: str) -> dict[str, int]:
  """
  Returns a dictionary of words mapped to the number of occurances of that word.
  """
  occurances = {}
  for word in sentence.split():
    if word in occurances:
      occurances[word] += 1
    else:
      occurances[word] = 1
  return occurances 

def test_word_occurance():
  assert(word_occurance('') == {})
  assert(word_occurance('a') == {'a': 1})
  assert(word_occurance('ab') == {'ab': 1})
  assert(word_occurance('a b') == {'a': 1, 'b': 1})
  assert(word_occurance('a a') == {'a': 2})
  assert(word_occurance('word is nice word') == {'word': 2, 'is': 1, 'nice': 1})