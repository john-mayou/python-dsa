class CreditCard:
    def __init__(self, customer: str, bank: str, account: str, limit: float, apr: float):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.apr = apr
        self.balance = 0
        self.minimum_payment = 35
        self.monthly_payment = 0
        
    def charge(self, price: float) -> bool:
        if price + self.balance > self.limit:
            return False
        self.balance += price
        return True
    
    def make_payment(self, amount: float) -> None:
        self.monthly_payment += amount
        self.balance -= amount
        
    def process_month(self) -> None:
        if self.balance > 0 and self.monthly_payment < self.minimum_payment:
            self.balance *= pow(1 + self.apr, 1/12)
        self.monthly_payment = 0
            
def test_credit_card():
    # meets monthly minimum
    cc = CreditCard('John', 'WF', 'Checking', 100, 0.20)
    for _ in range(5): cc.charge(10)
    cc.make_payment(30)
    cc.process_month()
    assert(round(cc.balance, 2) == 20.31)
    
    # does not meet monthly minimum
    cc = CreditCard('John', 'WF', 'Checking', 100, 0.20)
    for _ in range(5): cc.charge(10)
    cc.make_payment(40)
    cc.process_month()
    assert(cc.balance == 10)