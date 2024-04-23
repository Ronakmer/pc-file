import sqlite3

con = sqlite3.connect('students.db')

def create_table():
    con.execute("""CREATE TABLE IF NOT EXISTS students (
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              NAME TEXT,
              AGE INTEGER,
              CITY TEXT
              )""")
    con.commit()
    print("Table created successfully")

# Call the create_table function to ensure the table exists
create_table()

# Rest of your code goes here...


