import pandas as pd
import pyodbc

# Read Excel
df = pd.read_excel("students.xlsx")

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# SQL Server connection
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=BT07612\\SQLEXPRESS;"
    "DATABASE=login_system;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO students
        (StudentID, name, age, email, Department, GPA, GraduationYear)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        int(row["studentid"]),
        row["name"],
        int(row["age"]),
        row["email"],
        row["department"],
        float(row["gpa"]),
        int(row["graduationyear"])
    )

conn.commit()
cursor.close()
conn.close()

print("✅ Students inserted successfully")

