def factors1(n):
  """
  First implementation from the book.
  """
  results = []
  for k in range(1, n + 1):
    if n % k == 0:
      results.append(k)
  return results

def factors2(n):
  """
  Second implementation from the book.
  """
  for k in range(1, n + 1):
    if n % k == 0:
      yield k

def factors3(n):
  """
  Third implementation from the book.
  """
  k = 1
  while k * k < n:
    if n % k == 0:
      yield k
      yield n // k
    k += 1
  if k * k == n:
    yield k
    
def factors4(n):
  """
  Improves the third implementation by yeilding the factors in ascending order.
  """
  
  # yield factors under sqrt(n) and find quotients
  k, quotients = 1, []
  while k * k < n:
    if n % k == 0:
      yield k
      quotients.append(n // k)
    k += 1
    
  # perfect square case
  if k * k == n:
    yield k
  
  # yield quotients
  quotients.reverse()
  for q in quotients:
    yield q
    
def factors5(n):
  """
  Improves the third implementation by yielding the factors in ascending order using a recursive approach.
  """
  def inner(k):
    if k * k > n:
      return
    if n % k == 0:
      yield k
      if k * k != n:
        yield from inner(k + 1)
        yield n // k
    else:
      yield from inner(k + 1)
      
  yield from inner(1)
    
def test_factors4():
  assert(list(factors4(100)) == [1, 2, 4, 5, 10, 20, 25, 50, 100])
  assert(list(factors5(100)) == [1, 2, 4, 5, 10, 20, 25, 50, 100])