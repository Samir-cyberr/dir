import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('chinook.db')

# First check what tables exist
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Available tables:", cursor.fetchall())

# Then try to read the table (with possible case variations)
try:
    customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
    print(customers_df.head())
except:
    try:
        customers_df = pd.read_sql_query("SELECT * FROM Customers", conn)
        print(customers_df.head())
    except Exception as e:
        print("Error:", e)
finally:
    conn.close()