def power(x, n):
    if n == 0: return 1
    return x * power(x, n - 1)

power(2, 4)

# power(2, 5) -> 2*(16) = 32
# power(2, 4) -> 2*(8) = 16
# power(2, 3) -> 2*(4) = 8
# power(2, 2) -> 2*(2) = 4
# power(2, 1) -> 2*(1) = 2
# power(2, 0) -> 1