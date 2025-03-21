def harmonic(n):
    if n == 1: return 1
    return (1/n) + harmonic(n-1)

def test_harmonic():
    assert(harmonic(1) == 1)
    assert(harmonic(2) == 1.5)
    assert(round(harmonic(3), 2) == 1.83)