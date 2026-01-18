from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SERVER = "localhost\\SQLEXPRESS"
DATABASE = "login_system"
DRIVER = "ODBC Driver 17 for SQL Server"

DATABASE_URL = (
    f"mssql+pyodbc://{SERVER}/{DATABASE}"
    f"?driver={DRIVER.replace(' ', '+')}&trusted_connection=yes"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

