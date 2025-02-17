from typing import Self

class Progression():
    def __init__(self: Self, start: int = 0) -> None:
        self._current = start
        
    def _advance(self: Self) -> None:
        self._current += 1
        
    def __next__(self: Self) -> int:
        result = self._current
        self._advance()
        return result
        
    def __iter__(self: Self) -> Self:
        return self
    
class Fibonacci(Progression):
    def __init__(self: Self, first: int = 0, second: int = 1) -> None:
        super().__init__(first)
        self._prev = second - first
        
    def _advance(self: Self) -> None:
        self._prev, self._current = self._current, self._prev + self._current
        
def test_fibonacci():
    f = Fibonacci(2, 2)
    assert([next(f) for _ in range(8)] == [2, 2, 4, 6, 10, 16, 26, 42])