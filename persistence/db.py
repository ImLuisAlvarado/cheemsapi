import mysql.connector

def get_conecction():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="admin",
        database="cheemsdb"
    )