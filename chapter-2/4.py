class Flower():
    def __init__(self, name: str, petal_count: int, price: float) -> None:
        self._name = name
        self._petal_count = petal_count
        self._price = price
        
    def get_name(self) -> str:
        return self._name
    
    def get_petal_count(self) -> int:
        return self._petal_count
    
    def get_price(self) -> float:
        return self._price

def test_flower():
    flower = Flower('Rose', 50, 19.99)
    assert(flower.get_name() == 'Rose')
    assert(flower.get_petal_count() == 50)
    assert(flower.get_price() == 19.99)