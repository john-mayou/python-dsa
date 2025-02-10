def test_question():
  # This does not work because int values are immutable, thus it creates
  # a new int value that is not within the list.
  def scale(l: list[int], factor: int) -> list[int]:
    for n in l:
      n *= factor
    return l
  
  # This works because its assigning a new value at each given index.
  def scale2(l: list[int], factor: int) -> list[int]:
    for i in range(len(l)):
      l[i] *= factor
    return l
  
  input, factor = [1, 2, 3, 4], 2
  assert(scale(input, factor) == input) # original value
  assert(scale2(input, factor) == [2, 4, 6, 8]) # scaled