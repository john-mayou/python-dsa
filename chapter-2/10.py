from typing import Self

class Vector():
    def __init__(self, d: int) -> None:
        self._coords = [0] * d
        
    def __len__(self) -> int:
        return len(self._coords)
    
    def __getitem__(self, j: int) -> int:
        return self._coords[j]
    
    def __setitem__(self, j, val) -> None:
        self._coords[j] = val
        
    def __neg__(self) -> Self:
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result
    
    def __eq__(self, other: Self) -> bool:
        return self._coords == other._coords
    
def test_vector():
    v = Vector(3)
    v[0] = 1
    v[1] = 2
    v[2] = 3
    
    ex = Vector(3)
    ex[0] = -1
    ex[1] = -2
    ex[2] = -3
    
    assert(-v == ex)