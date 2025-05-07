import sqlite3

def create_database():
    """Create the database and table structure"""
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Create Books table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Books
                      (Title TEXT, Author TEXT, Year_Published INTEGER, Genre TEXT, Rating REAL)''')

    # Clear existing data to avoid duplicate insertions (optional, but useful for re-running)
    cursor.execute("DELETE FROM Books")

    # Insert initial data
    initial_data = [
        ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
        ('1984', 'George Orwell', 1949, 'Dystopian'),
        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
    ]
    cursor.executemany("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)", initial_data)

    conn.commit()
    conn.close()

def update_data():
    """Update the publication year of 1984"""
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")

    conn.commit()
    conn.close()

def query_dystopian():
    """Query and display Dystopian books"""
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
    dystopian_books = cursor.fetchall()

    print("\nDystopian Books:")
    for title, author in dystopian_books:
        print(f"Title: {title}, Author: {author}")

    conn.close()

def delete_pre_1950():
    """Delete books published before 1950"""
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")

    conn.commit()
    conn.close()

def add_rating_column():
    """Add Rating column and update values"""
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Check if 'Rating' column already exists
    cursor.execute("PRAGMA table_info(Books)")
    columns = [info[1] for info in cursor.fetchall()]
    if 'Rating' not in columns:
        cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")

    # Update ratings
    ratings = [
        (4.8, 'To Kill a Mockingbird'),
        (4.7, '1984'),
        (4.5, 'The Great Gatsby')
    ]
    cursor.executemany("UPDATE Books SET Rating = ? WHERE Title = ?", ratings)

    conn.commit()
    conn.close()

def query_sorted_by_year():
    """Query all books sorted by publication year ascending"""
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute("SELECT Title, Author, Year_Published, Genre, Rating FROM Books ORDER BY Year_Published ASC")
    books = cursor.fetchall()

    print("\nBooks Sorted by Publication Year (Ascending):")
    for title, author, year, genre, rating in books:
        print(f"Title: {title}, Author: {author}, Year: {year}, Genre: {genre}, Rating: {rating}")

    conn.close()

def main():
    # Task 1: Database Creation
    create_database()

    # Update Data
    update_data()

    # Query Data
    query_dystopian()

    # Delete Data
    delete_pre_1950()

    # Bonus Task: Add Rating column
    add_rating_column()

    # Advanced Query
    query_sorted_by_year()

if __name__ == "__main__":
    main()
