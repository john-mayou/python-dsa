from __future__ import annotations

class Wallet:
    def __init__(self, usd: float):
        self.usd = usd
        
    def charge(self, amount: float) -> bool:
        if self.usd - amount < 0:
            return False
        self.usd -= amount
        return True
        
    def recharge(self, amount: float):
        self.usd += amount

class Person:
    def __init__(self, collection: Collection, wallet: Wallet):
        self.collection = collection
        self.wallet = wallet
    
class Book:
    def __init__(self, title: str, content: str, price: float, electronic: bool = True):
        self.title = title
        self.content = content
        self.price = price
        self.electronic = electronic
    
class Collection:
    def __init__(self, books: list[Book] = []):
        self.books = books
        
    def add_book(self, book: Book):
        self.books.append(book)
        
class BookStore:
    def __init__(self):
        pass
    
    def buy_book(self, person: Person, book: Book):
        purchased = person.wallet.charge(book.price)
        if purchased:
            person.collection.add_book(book)
        else:
            raise RuntimeError("Insufficient funds available to purchase book")

def main():
    p = Person(Collection(), Wallet(65))
    
    b1 = Book('Hunger Games', 'content', 20.0, True)
    b2 = Book('Hunger Games: Catching Fire', 'content', 20.0, True)
    b3 = Book('Hunger Games: Mockingjay', 'content', 20.0, True)
    
    s = BookStore()
    s.buy_book(p, b1)
    s.buy_book(p, b2)
    s.buy_book(p, b3)
    
    assert(p.collection.books == [b1, b2, b3])
    assert(p.wallet.usd == 5)

def test_main(): main()