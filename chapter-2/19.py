from typing import Self

class Progression():
    def __init__(self: Self, start: int = 0) -> None:
        self.current = start
        
    def advance(self: Self) -> None:
        self.current += 1
        
    def __next__(self: Self) -> None:
        result = self.current
        self.advance()
        return result
    
    def __iter__(self: Self) -> Self:
        return self
    
class Arithmetic(Progression):
    def __init__(self: Self, increment: int = 1, start: int = 0) -> None:
        super().__init__(start)
        self.increment = increment
        
    def advance(self: Self) -> None:
        self.current += self.increment
        
def test_arithmetic():
    iterations = 0
    progression = Arithmetic(128, 0)
    while True:
        val = next(progression)
        iterations += 1
        if val >= 263: break
        
    assert iterations == 4
        