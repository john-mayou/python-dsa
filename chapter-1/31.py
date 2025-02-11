CENT_1 = 'penny'
CENT_5 = 'nickel'
CENT_10 = 'dime'
CENT_25 = 'quarter'
CENT_50 = 'half dollar'
DOLLAR_1 = '1 dollar'
DOLLAR_5 = '5 dollars'
DOLLAR_10 = '10 dollars'
DOLLAR_20 = '20 dollars'
DOLLAR_50 = '50 dollars'
DOLLAR_100 = '100 dollars'

DENOMINATIONS = [
  (100, DOLLAR_100), (50, DOLLAR_50), (20, DOLLAR_20), (10, DOLLAR_10), (5, DOLLAR_5), (1, DOLLAR_1),
  (0.5, CENT_50), (0.25, CENT_25), (0.1, CENT_10), (0.05, CENT_5), (0.01, CENT_1)
]

def get_change(charged: float, given: float) -> float:
  """
  Finds the appropriate denominations to return based on the change to return.
  """
  
  change = []
  change_left = round(given - charged, 2)
  
  for value, name in DENOMINATIONS:
    while change_left >= value:
      change.append(name)
      change_left = round(change_left - value, 2)
    
  return change

def test_get_change():
  assert(get_change(1, 1) == [])
  assert(get_change(1, 1.94) == [CENT_50, CENT_25, CENT_10, CENT_5, CENT_1, CENT_1, CENT_1, CENT_1])
  assert(get_change(1, 20) == [DOLLAR_10, DOLLAR_5, DOLLAR_1, DOLLAR_1, DOLLAR_1, DOLLAR_1])
  assert(get_change(1, 122) == [DOLLAR_100, DOLLAR_20, DOLLAR_1])
  assert(get_change(5.25, 19) == [DOLLAR_10, DOLLAR_1, DOLLAR_1, DOLLAR_1, CENT_50, CENT_25])