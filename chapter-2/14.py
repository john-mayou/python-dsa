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
        if isinstance(other, (int, float)):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
            return result
        elif isinstance(other, Vector):
            result = 0
            for j in range(len(self)):
                result += self[j] * other[j]
            return result
        return NotImplemented
    
    def __rmul__(self, other: Union[int, float]) -> Self:
        return self.__mul__(other)
    
    def __eq__(self, other: Self) -> bool:
        return self._coords == other._coords
    
def test_vector():
    v = Vector(3)
    v[0], v[1], v[2] = 1, 2, 3
    
    ex = Vector(3)
    ex[0], ex[1], ex[2] = 3, 6, 9
    
    assert(v * 3 == ex)
    assert(3 * v == ex)
    
    v2 = Vector(3)
    v2[0], v2[1], v2[2] = 2, 3, 4
    
    assert(v * v2 == 20)
    assert(v2 * v == 20)