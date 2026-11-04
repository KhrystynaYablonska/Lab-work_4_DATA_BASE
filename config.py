import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="7101.Khr",
        database="lung_health_db"
    )