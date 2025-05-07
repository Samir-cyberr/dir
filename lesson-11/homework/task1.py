import sqlite3

def create_database():
    """Create the database and table structure"""
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()
    
    # Create Roster table with Rank column included from the beginning
    cursor.execute('''CREATE TABLE IF NOT EXISTS Roster
                      (Name TEXT, Species TEXT, Age INTEGER, Rank TEXT)''')
    
    # Clear existing data to avoid duplicates on re-run
    cursor.execute("DELETE FROM Roster")
    
    # Insert initial data (Rank will be NULL for now)
    initial_data = [
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys', 'Bajoran', 29)
    ]
    cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", initial_data)
    
    conn.commit()
    conn.close()

def update_data():
    """Update Jadzia Dax to Ezri Dax"""
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()
    
    cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")
    
    conn.commit()
    conn.close()

def query_bajorans():
    """Query and display Bajoran characters"""
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    bajorans = cursor.fetchall()
    
    print("\nBajoran Characters:")
    for name, age in bajorans:
        print(f"Name: {name}, Age: {age}")
    
    conn.close()

def delete_over_100():
    """Delete characters over 100 years old"""
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM Roster WHERE Age > 100")
    
    conn.commit()
    conn.close()

def add_rank_column():
    """Add Rank column and update values"""
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()
    
    # Check if Rank column already exists
    cursor.execute("PRAGMA table_info(Roster)")
    columns = [col[1] for col in cursor.fetchall()]
    if 'Rank' not in columns:
        cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
    
    # Update ranks
    ranks = [
        ('Captain', 'Benjamin Sisko'),
        ('Lieutenant', 'Ezri Dax'),
        ('Major', 'Kira Nerys')
    ]
    cursor.executemany("UPDATE Roster SET Rank = ? WHERE Name = ?", ranks)
    
    conn.commit()
    conn.close()

def query_sorted_by_age():
    """Query all characters sorted by age descending"""
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT Name, Age, Species, Rank FROM Roster ORDER BY Age DESC")
    characters = cursor.fetchall()
    
    print("\nCharacters Sorted by Age (Descending):")
    for name, age, species, rank in characters:
        print(f"Name: {name}, Age: {age}, Species: {species}, Rank: {rank}")
    
    conn.close()

def main():
    create_database()
    update_data()
    query_bajorans()
    delete_over_100()
    add_rank_column()
    query_sorted_by_age()

if __name__ == "__main__":
    main()
