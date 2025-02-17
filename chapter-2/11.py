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
        
    def __add__(self, other: Self) -> Self:
        if len(self) != len(other):
            raise ValueError(f"dimensions must match: {len(self)} != {len(other)}")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __radd__(self, other: Self) -> Self:
        return self.__add__(other)
    
    def __eq__(self, other: Self) -> bool:
        return self._coords == other._coords
    
def test_vector():
    v = Vector(3)
    v[0] = 1
    v[1] = 2
    v[2] = 3
    
    l = [1, 2, 3]
    
    ex = Vector(3)
    ex[0] = 2
    ex[1] = 4
    ex[2] = 6
    
    assert(v + l == ex)
    assert(l + v == ex)