import os , psycopg2
from dotenv import load_dotenv
load_dotenv()

def get_db_connection():
    """
    Establishes a connection to the PostgreSQL database.
    Returns: connection object or None if failed.
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error Connecting to Database: {e}")
        return None