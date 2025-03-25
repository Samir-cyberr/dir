class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def __str__(self):
        return f"'{self.title}' by {self.author} - {'Borrowed' if self.is_borrowed else 'Available'}"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def can_borrow(self):
        return len(self.borrowed_books) < 3
    
    def borrow_book(self, book):
        if not self.can_borrow():
            raise MemberLimitExceededException(f"{self.name} has already borrowed the maximum of 3 books.")
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            raise BookNotFoundException(f"{self.name} didn't borrow '{book.title}'")

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def add_member(self, member):
        self.members.append(member)
    
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def find_member(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        return None
    
    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        
        if not member:
            print(f"Member {member_name} not found.")
            return
        if not book:
            raise BookNotFoundException(f"Book '{book_title}' not found in the library.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"Book '{book_title}' is already borrowed.")
        if not member.can_borrow():
            raise MemberLimitExceededException(f"{member_name} has already borrowed the maximum of 3 books.")
        
        book.is_borrowed = True
        member.borrow_book(book)
        print(f"{member_name} has successfully borrowed '{book_title}'.")
    
    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        
        if not member:
            print(f"Member {member_name} not found.")
            return
        if not book:
            raise BookNotFoundException(f"Book '{book_title}' not found in the library.")
        if not book.is_borrowed:
            print(f"Book '{book_title}' is not currently borrowed.")
            return
        
        try:
            member.return_book(book)
            book.is_borrowed = False
            print(f"{member_name} has successfully returned '{book_title}'.")
        except BookNotFoundException as e:
            print(e)

# Testing the library system
def test_library_system():
    library = Library()
    
    # Add books
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("Pride and Prejudice", "Jane Austen"))
    
    # Add members
    library.add_member(Member("Alice"))
    library.add_member(Member("Bob"))
    
    # Test scenarios
    print("\n--- Testing normal borrowing ---")
    library.borrow_book("Alice", "The Great Gatsby")
    library.borrow_book("Bob", "1984")
    
    print("\n--- Testing exceptions ---")
    try:
        library.borrow_book("Alice", "Unknown Book")
    except BookNotFoundException as e:
        print(f"Error: {e}")
    
    try:
        library.borrow_book("Alice", "1984")  # Already borrowed by Bob
    except BookAlreadyBorrowedException as e:
        print(f"Error: {e}")
    
    # Alice borrows 2 more books to reach limit
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "Pride and Prejudice")
    
    try:
        library.borrow_book("Alice", "1984")  # Should fail due to limit
    except MemberLimitExceededException as e:
        print(f"Error: {e}")
    
    print("\n--- Testing returning books ---")
    library.return_book("Alice", "The Great Gatsby")
    library.return_book("Bob", "1984")
    
    try:
        library.return_book("Alice", "Unknown Book")
    except BookNotFoundException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_library_system()