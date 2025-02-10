import random

def shuffle2(l: list[int]) -> list[int]:
  """
  Returns `l` with its values randomly shuffled in place.
  """
  for i in range(len(l)):
    newi = random.randint(0, len(l) - 1)
    l[i], l[newi] = l[newi], l[i]
  return l

def test_shuffle2():
  l = [1, 2, 3, 4, 5]
  for _ in range(10):
    print(shuffle2(l))