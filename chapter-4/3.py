def power(x: int, n: int) -> int:
    """
    (x^(n/2))^2 | if n is even
    x * x^(n-1) | if n is odd
    
    Time -> O(log(n))
    Space -> O(log(n))
    """
    if n == 0: return 1
    if n == 1: return x
    partial = power(x, n // 2)
    result = partial * partial
    if n % 2 == 1: result *= x
    return result

def test_power():
    assert(power(2, 0) == 1)
    assert(power(2, 1) == 2)
    assert(power(2, 2) == 4)
    assert(power(2, 3) == 8)
    assert(power(2, 4) == 16)
    
# power(2, 18) -> 512*512=262144
# power(2, 9) -> 16*16*2=512
# power(2, 4) -> 4*4=16
# power(2, 2) -> 2*2=4
# power(2, 1) -> 2