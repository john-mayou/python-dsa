"""
a) p(x) can be O(n^2) if as we multiply terms of different degress together:
  x + x*x + x*x*x ... (1+2+3...) = O(n^2)
  
b) p(x) can be O(nlog(n)) if we can use the following strategy:
  (x^(n/2))^2 if n is even O(log(n))
  (x*x^(n-1)) if n is odd  O(log(n)+1)
  thus, asymptotically for every n we do log(n) work: O(nlog(n))
  
c) p(x) can be O(n) if we Horner's method (shown below)
"""

def algo(coeffs, x):
    result = coeffs[0]
    for i in range(1, len(coeffs)):
        result = result * x + coeffs[i]
    return result
        
    
def test_algo():
    assert(algo([7, 5, 2, 3], 2) == 83)
    # (2 * (2 * (7 * 2 + 5) + 2) + 3)