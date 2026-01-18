import pyodbc

# 1. Take login input
email = input("Enter Email: ")
password = input("Enter Password: ")

# 2. Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=login_system;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# 3. Check credentials
cursor.execute("""
    SELECT id FROM teachers
    WHERE email = ? AND password = ?
""", email, password)

result = cursor.fetchone()

# 4. Login result
if result:
    print("✅ Login successful!")
    print("Welcome, Teacher ID:", result[0])
else:
    print("❌ Invalid email or password")

cursor.close()
conn.close()
