from typing import Union

class CreditCard():
    def __init__(self, customer: str, bank: str, account: str, limit: Union[int, float], balance: Union[int, float] = 0) -> None:
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = balance
        
    def charge(self, price: Union[int, float]) -> None:
        if price + self.balance > self.limit:
            return False
        self.balance += price
        return True
    
    def make_payment(self, amount: Union[int, float]) -> None:
        self.balance -= amount

def test_credit_card():
    cc = CreditCard('John', 'WF', 'Checking', 100)
    cc.charge(50)
    cc.make_payment(20)
    assert(cc.balance == 30)
    
    cc = CreditCard('John', 'WF', 'Checking', 100, 20)
    cc.charge(50)
    cc.make_payment(20)
    assert(cc.balance == 50)