from typing import Union

def maxx(S: list[int]) -> Union[None, int]:
    if len(S) == 0: return None
    
    def maxxHelper(curr_max, curr_i):
        if curr_i >= len(S): return curr_max
        if S[curr_i] > curr_max: curr_max = S[curr_i]
        return maxxHelper(curr_max, curr_i + 1)
    
    return maxxHelper(S[0], 1)

def test_maxx():
    assert(maxx([]) == None)
    assert(maxx([0]) == 0)
    assert(maxx([0, 1]) == 1)
    assert(maxx([1, 0]) == 1)
    assert(maxx([1, 2, 3]) == 3)
    assert(maxx([1, 2, 3, 4]) == 4)
    assert(maxx([4, 3, 2, 1]) == 4)
    assert(maxx([4, 4, 4, 4]) == 4)