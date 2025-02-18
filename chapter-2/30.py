class CreditCard:
    def __init__(self, customer: str, bank: str, account: str, limit: float):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = 0
        
    def get_balance(self) -> float:
        return self.balance
    
    def set_balance(self, balance: float) -> None:
        self.balance = balance
        
    def charge(self, price: float) -> bool:
        if price + self.balance > self.limit:
            return False
        self.balance += price
        return True
    
    def make_payment(self, amount: float) -> None:
        self.balance -= amount
        
    def process_month(self) -> None:
        if self.balance > 0:
            self.balance *= pow(1 + self.apr, 1/12)