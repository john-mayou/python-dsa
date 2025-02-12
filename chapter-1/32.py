from typing import Union
from enum import Enum

class Operator(str, Enum):
  PLUS = '+'
  MINUS = '-'
  STAR = '*'
  SLASH = '/'

def calculate(terms: list[Union[int, float, Operator]]) -> float:
  """
  Calculates the mathematical equation based on the expression `terms`.
  """
  
  if len(terms) == 0: return 0
  if not isinstance(terms[0], Union[int, float]):
    raise Exception(f"First term must be a number but got: {terms[0]}")
  if len(terms) == 1: return terms[0]
  
  total = terms[0]
  i = 1
  while i <= len(terms) - 2:
    op, n = terms[i], terms[i + 1]
    match op:
      case Operator.PLUS: total += n
      case Operator.MINUS: total -= n
      case Operator.STAR: total *= n
      case Operator.SLASH: total /= n
      case _: raise Exception(f"Invalid operator: {op}")
    i += 2
  
  return total

def test_calculate():
  assert(calculate([]) == 0)
  assert(calculate([0]) == 0)
  assert(calculate([1]) == 1)
  assert(calculate([2, Operator.PLUS, 2]) == 4)
  assert(calculate([2, Operator.MINUS, 2]) == 0)
  assert(calculate([2, Operator.STAR, 2]) == 4)
  assert(calculate([2, Operator.SLASH, 2]) == 1)
  assert(calculate([2, Operator.PLUS, 2, Operator.STAR, 2]) == 8)
  

def main():
  terms = []
  while True:
    try:
      # number
      while True:
        try:
          terms.append(float(input('Enter a number: ')))
          break
        except ValueError: continue
        
      # operation
      while True:
        op_raw = input('Enter an operation (+ - * /): ')
        try:
          terms.append(Operator(op_raw))
          break
        except ValueError: continue
    except EOFError: # Mac: Control + D
      break
    
  print(f"\nTotal is {calculate(terms)}")

if __name__ == "__main__": main()