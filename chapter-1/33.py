from enum import Enum

class Operator(str, Enum):
  PLUS = '+'
  MINUS = '-'
  STAR = '*'
  SLASH = '/'

def prompt_number() -> float:
  while True:
    try: return float(input('Enter a number: '))
    except ValueError: continue
    
def prompt_operator() -> Operator:
  while True:
    try: return Operator(input('Enter an operator (+ - * /): '))
    except ValueError: continue

def calculate(terms: tuple[float, Operator, float]) -> float:
  t1, op, t2 = terms
  match op:
    case Operator.PLUS: return t1 + t2
    case Operator.MINUS: return t1 - t2
    case Operator.STAR: return t1 * t2
    case Operator.SLASH: return t1 / t2
    case _: raise Exception(f"Invalid operator: {op}")

def main():
  total = None
  while True:
    try:
      if total is None: total = prompt_number()
      op = prompt_operator()
      t2 = prompt_number()
      new_total = calculate((total, op, t2))
      print(f"{total} {op.value} {t2} = {new_total}")
      total = new_total
    except EOFError:
      total = None
      print("\nReset complete.")
  
if __name__ == "__main__": main()