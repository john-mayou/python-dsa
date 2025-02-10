import random

def choice2(l):
  """
  Implements random.choice using random.randrange.
  """
  return l[random.randrange(len(l))]

def test_choice2():
  l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  for _ in range(10):
    print(choice2(l))