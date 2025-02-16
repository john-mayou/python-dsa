from typing import Union

class CreditCard():
    def __init__(self, customer: str, bank: str, account: str, limit: Union[int, float]):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = 0
        
    def charge(self, price: Union[int, float]) -> None:
        if not isinstance(price, (int, float)):
            raise ValueError(f"price must be numeric but got {type(price)}")
        if price + self.balance > self.limit:
            return False
        self.balance += price
        return True
    
    def make_payment(self, amount: Union[int, float]) -> None:
        if not isinstance(amount, (int, float)):
            raise ValueError(f"amount must be numeric but got {type(amount)}")
        self.balance -= amount

def test_credit_card():
    cc = CreditCard('John', 'WF', 'Checking', 100)
    cc.charge(50)
    cc.make_payment(20)
    assert(cc.balance == 30)
    
    fail = False
    try:
        cc.charge('hot dog')
        fail = True
    except ValueError:
        pass
    assert(fail == False)
    
    fail = False
    try:
        cc.make_payment('hot dog')
        fail = True
    except ValueError:
        pass
    assert(fail == False)
        