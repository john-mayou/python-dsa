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
        
    def __sub__(self, other: Self) -> Self:
        if len(self) != len(other):
            raise ValueError(f"dimentions must agree: {len(self)} != {len(other)}")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    
    def __eq__(self, other: Self) -> bool:
        return self._coords == other._coords
    
def test_vector():
    v1 = Vector(3)
    v1[0] = 1
    v1[1] = 2
    v1[2] = 3
    
    v2 = Vector(3)
    v2[0] = 3
    v2[1] = 1
    v2[2] = 3
    
    ex = Vector(3)
    ex[0] = -2
    ex[1] = 1
    ex[2] = 0
    
    assert(v1 - v2 == ex)