import pyodbc

# 1. Take user input
teacher_id = int(input("Enter Teacher ID: "))
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

# 3. Update email & password for that teacher
cursor.execute("""
    UPDATE teachers
    SET email = ?, password = ?
    WHERE id = ?
""", email, password, teacher_id)

conn.commit()

# 4. Check if update happened
if cursor.rowcount == 0:
    print("❌ No teacher found with this ID")
else:
    print("✅ Email & password updated successfully")

cursor.close()
conn.close()


