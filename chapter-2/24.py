class Book():
    def __init__(self, title: str, content: dict[int, str], page_count: int) -> None:
        self.title = title
        self.content = content
        self.page_count = page_count
        
    def page_content(self, page_number: int) -> str:
        if self.page_count < page_number:
            raise ValueError(f"page number cannot be higher than the page count: {page_number} > {self.page_count}")
        content = self.content.get(page_number)
        if content == None:
            raise RuntimeError(f"no content found for page number {page_number}")
        return content
    
class Collection():
    def __init__(self, books: list[Book]) -> None:
        self.collection = books
    
    def add_book(self, book: Book) -> None:
        self.collection.append(book)

class Store():
    def __init__(self, catalog: list[Book]) -> None:
        self.catalog = catalog
    
    def get_catalog(self) -> list[Book]:
        return self.catalog
    
    def buy_book(book: Book, collection: Collection) -> None:
        collection.add_book(book)
        
class Reader():
    def __init__(self, book: Book):
        self.book = book
        self.current_page = 0
        
    def next_page(self) -> None:
        self.read_page(self.current_page + 1)
        
    def read_page(self, page_number: int) -> None:
        self.current_page = page_number
        print(self.book.page_content(page_number))