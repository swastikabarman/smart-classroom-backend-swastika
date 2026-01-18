import pyodbc
import bcrypt

# User input
email = input("Enter email: ").strip()
password = input("Create password: ").strip()

hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# DB connection
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=BT07612\\SQLEXPRESS;"
    "DATABASE=login_system;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# Check if email exists
cursor.execute("SELECT id FROM students WHERE email = ?", email)
user = cursor.fetchone()

if user:
    # Existing student → update password
    cursor.execute("""
        UPDATE students
        SET password = ?
        WHERE email = ?
    """, hashed_password, email)
    print("✅ Signup complete (existing user)")
else:
    # New student → insert minimal record
    cursor.execute("""
        INSERT INTO students (email, password)
        VALUES (?, ?)
    """, email, hashed_password)
    print("✅ Signup complete (new user)")

conn.commit()
cursor.close()
conn.close()

