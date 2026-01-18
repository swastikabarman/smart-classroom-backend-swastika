import pyodbc
import bcrypt

# User input
email = input("Email: ").strip()
password = input("Password: ").strip()

# DB connection
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=BT07612\\SQLEXPRESS;"
    "DATABASE=login_system;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# Fetch hashed password
cursor.execute("""
    SELECT password, name
    FROM students
    WHERE email = ?
""", email)

user = cursor.fetchone()

if not user:
    print("❌ Email not registered")
else:
    stored_hash, name = user

    if stored_hash is None:
        print("⚠️ Please signup first")
    elif bcrypt.checkpw(password.encode(), stored_hash.encode()):
        print(f"✅ Login successful! Welcome {name}")
    else:
        print("❌ Incorrect password")

cursor.close()
conn.close()
