from typing import Self

class Goat(object):
    def __init__(self: Self) -> None:
        self._tail = None
        
    def milk(self: Self) -> None:
        pass
    
    def jump(self: Self) -> None:
        pass
    
class Pig(object):
    def __init__(self: Self) -> None:
        self._nose = None
        
    def eat(self: Self, food: str) -> None:
        pass
    
    def wallow(self: Self) -> None:
        pass
    
class Horse(object):
    def __init__(self: Self) -> None:
        self._height = None
        
    def run(self: Self) -> None:
        pass
    
    def jump(self: Self) -> None:
        pass
    
class Racer(Horse):
    def race(self: Self) -> None:
        pass
    
class Equestrian(Horse):
    def __init__(self: Self) -> None:
        super().__init__()
        self._weight = None
        
    def trot(self: Self) -> None:
        pass
    
    def is_trained(self: Self) -> bool:
        return True