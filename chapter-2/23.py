from abc import ABCMeta, abstractmethod
from typing import Self, Any

class Sequence(metaclass = ABCMeta):
    @abstractmethod
    def __len__(self: Self) -> int:
        pass
    
    @abstractmethod
    def __getitem__(self: Self, j: int) -> Any:
        pass
    
    def __lt__(self: Self, other: Self) -> bool:
        if not isinstance(other, Sequence):
            raise ValueError("must compare against another sequence")

        for i in range(min(len(self), len(other))):
            if self[i] != other[i]:
                return self[i] < other[i]
        
        return len(self) < len(other)
    
class List(Sequence):
    def __init__(self: Self, values: list) -> None:
        self._values = values
    
    def __len__(self: Self) -> int:
        return len(self._values)
        
    def __getitem__(self: Self, j: int) -> Any:
        return self._values[j]
    
def test_sequence():
    assert(List([1, 2]) < List([1, 2, 3]))
    assert(not List([1, 2, 3]) < List([1, 2]))
    assert(List([1, 2, 2]) < List([1, 2, 3]))
    assert(not List([1, 2, 3]) < List([1, 2, 2]))
    assert(not List([1, 2, 3]) < List([1, 2, 3]))
    assert(List([1, 2, 3]) < List([1, 2, 4]))