class CreditCard:
    def __init__(self, customer: str, bank: str, account: str, limit: float, apr: float):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.apr = apr
        self.balance = 0
        self.monthly_charges = 0
        
    def charge(self, price: float) -> bool:
        if price + self.balance > self.limit:
            return False
        self.monthly_charges += 1
        self.balance += price
        return True
    
    def make_payment(self, amount: float) -> None:
        self.balance -= amount
        
    def process_month(self) -> None:
        if self.balance > 0:
            self.balance *= pow(1 + self.apr, 1/12)
        charges = self.monthly_charges
        while (charges > 10):
            self.balance += 1
            charges -= 1
            
def test_credit_card():
    cc = CreditCard('John', 'WF', 'Checking', 1000, 0.20)
    for _ in range(15): cc.charge(10)
    cc.process_month()
    assert(round(cc.balance, 2) == round(150 * pow(1.2, 1/12) + 5, 2))