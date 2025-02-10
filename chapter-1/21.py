def test_question():  
  # prompt user for words
  words = []
  while True:
    try:
      words.append(input('Enter a word: '))
    except EOFError: # Mac: Control + D
      print()
      break
  
  # reverse in place
  p1, p2 = 0, len(words) - 1
  while(p1 < p2):
    words[p1], words[p2] = words[p2], words[p1]
    p1 += 1
    p2 -= 1
    
  # print words
  for word in words:
    print(word)

test_question()