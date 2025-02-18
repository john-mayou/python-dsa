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
    
class DiffProgression(Progression):
    def __init__(self, first: int = 2, second: int = 200):
        self.current = first
        self.prev = first + second
        
    def _advance(self):
        self.prev, self.current = self.current, abs(self.current - self.prev)
        
def test_diff_progression():
    dp = DiffProgression(2, 200)
    assert([next(dp) for _ in range(10)] == [2, 200, 198, 2, 196, 194, 2, 192, 190, 2])
    dp = DiffProgression(-2, 200)
    assert([next(dp) for _ in range(10)] == [-2, 200, 202, 2, 200, 198, 2, 196, 194, 2])