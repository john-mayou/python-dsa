from typing import Self, Union

class Vector():
    def __init__(self, d: int) -> None:
        self._coords = [0] * d
        
    def __len__(self) -> int:
        return len(self._coords)
    
    def __getitem__(self, j: int) -> int:
        return self._coords[j]
    
    def __setitem__(self, j, val) -> None:
        self._coords[j] = val
    
    def __mul__(self, other: Union[int, float]) -> Self:
        if not isinstance(other, (int, float)):
            return NotImplemented
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * other
        return result
    
    def __rmul__(self, other: Union[int, float]) -> Self:
        return self.__mul__(other)
    
    def __eq__(self, other: Self) -> bool:
        return self._coords == other._coords
    
def test_vector():
    v = Vector(3)
    v[0] = 1
    v[1] = 2
    v[2] = 3
    
    ex = Vector(3)
    ex[0] = 3
    ex[1] = 6
    ex[2] = 9
    
    assert(v * 3 == ex)
    assert(3 * v == ex)