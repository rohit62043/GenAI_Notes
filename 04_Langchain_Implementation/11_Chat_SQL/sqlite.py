import sqlite3


# Step 1: Connect to the Database
# If student.db doesn't exist, it gets created automatically.
# Acts as the main gateway to interact with your database.
connection = sqlite3.connect("student.db")

#Step 2: Create a Cursor
# The cursor object is used to:
# Run SQL queries
# Fetch results
# Manage transactions
cursor=connection.cursor()

#  Step 3: Create the Table

sql_query="""
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INTEGER
)
"""
    
cursor.execute(sql_query)

#  Step 4: Insert Records
students_data = [
    ("Krish", "Data Science", "A", 90),
    ("John", "Data Science", "B", 85),
    ("Mukesh", "Data Science", "A", 78),
    ("Jacobs", "DevOps", "A", 50)
]

for student in students_data:
    cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?)", student)

#  Step 5: Fetch & Display Records

cursor.execute("SELECT * FROM STUDENT")
rows = cursor.fetchall()

print("The inserted records are:")
for row in rows:
    print(row)

#  Step 6: Commit and Close
connection.commit()    # Save all changes
connection.close()     # Always close the DB connection
