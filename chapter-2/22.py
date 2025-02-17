from abc import ABCMeta, abstractmethod
from typing import Self, Any

class Sequence(metaclass = ABCMeta):
    @abstractmethod
    def __len__(self: Self) -> int:
        pass
    
    @abstractmethod
    def __getitem__(self: Self, j: int) -> Any:
        pass
    
    def __eq__(self: Self, other: Self) -> bool:
        if not isinstance(other, Sequence): return False
        if len(self) != len(other): return False
        return all([self[i] == other[i] for i in range(len(self))])
    
class List(Sequence):
    def __init__(self: Self, values: list) -> None:
        self._values = values
    
    def __len__(self: Self) -> int:
        return len(self._values)
        
    def __getitem__(self: Self, j: int) -> Any:
        return self._values[j]
    
class Tuple(Sequence):
    def __init__(self: Self, values: tuple) -> None:
        self._values = values
    
    def __len__(self: Self) -> int:
        return len(self._values)
        
    def __getitem__(self: Self, j: int) -> Any:
        return self._values[j]
    
def test_sequence():
    assert(List([1, 2, 3]) == List([1, 2, 3]))
    assert(not (List([1, 2, 3]) == List([1, 2, 4])))
    
    assert(Tuple((1, 2, 3)) == Tuple((1, 2, 3)))
    assert(not (Tuple((1, 2, 3)) == Tuple((1, 2, 4))))