import math

class Progression:
    def __init__(self, start: int = 0):
        self.current = start
        
    def _advance(self):
        self.current += 1
        
    def __next__(self):
        result = self.current
        self._advance()
        return result
    
    def __list__(self):
        return self
    
class SquareRootProgression(Progression):
    def __init__(self, first: float = 65_536):
        self.current = first
        
    def _advance(self):
        self.current = math.sqrt(self.current)
        
def test_square_progression():
    p = SquareRootProgression()
    assert([next(p) for _ in range(5)] == [65_536, 256, 16, 4, 2])