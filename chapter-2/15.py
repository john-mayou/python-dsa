from typing import Self, Union, Iterable

class Vector():
    def __init__(self, d: Union[int, Iterable[int]]) -> None:
        if isinstance(d, int):
            self._coords = [0] * d
        elif isinstance(d, Iterable):
            self._coords = list(d)
        else:
            raise ValueError(f"Invalid `d` type: {type(d)}")
        
    def __len__(self) -> int:
        return len(self._coords)
    
    def __getitem__(self, j: int) -> int:
        return self._coords[j]
    
    def __setitem__(self, j, val) -> None:
        self._coords[j] = val
    
    def __eq__(self, other: Self) -> bool:
        return self._coords == other._coords
    
def test_vector():
    v = Vector(3)
    v[0], v[1], v[2] = 1, 2, 3
    assert(v == Vector([1, 2, 3]))
    assert(Vector(3) == Vector([0, 0, 0]))