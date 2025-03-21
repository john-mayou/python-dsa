def to_i(s: str) -> int:
    num_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def to_i_helper(total, index, degree):
        if index >= len(s): return total
        total += num_map[s[index]] * pow(10, degree)
        return to_i_helper(total, index + 1, degree - 1)
    return to_i_helper(0, 0, len(s) - 1)

def to_i2(s: str) -> int:
    num_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    total = 0
    degree = len(s) - 1
    for num_str in s:
        total += num_map[num_str] * pow(10, degree)
        degree -= 1
    return total   

def test_to_i():
    assert(to_i('') == 0)
    assert(to_i('0') == 0)
    assert(to_i('1') == 1)
    assert(to_i('12') == 12)
    assert(to_i('123') == 123)
    assert(to_i('13531') == 13531)
     
def test_to_i2():
    assert(to_i2('') == 0)
    assert(to_i2('0') == 0)
    assert(to_i2('1') == 1)
    assert(to_i2('12') == 12)
    assert(to_i2('123') == 123)
    assert(to_i2('13531') == 13531)