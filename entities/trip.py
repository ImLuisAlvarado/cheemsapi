from persistence.db import get_connection
from mysql.connector import Error

class Trip:

    def __init__(self, name, city, latitude, longitude):
        self.name = name
        self.city = city
        self.latitude = latitude
        self.longitude = longitude


    def get_all():
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary = True)
            cursor.execute('SELECT id, name, city, latitude, longitude FROM trip')
            return cursor.fetchall()
        except Error as ex:
            return str(ex)
        finally:
            cursor.close()
            connection.close()

    def save(self):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            sql = 'INSERT INTO trip  (name, city, latitude, longitude)  VALUES (%s, %s, %s, %s)'
            cursor.execute(sql, (self.name, self.city, self.latitude, self.longitude))
            connection.commit()
            return cursor.lastrowid
        except Error as ex:
            return str(ex)
        finally:
            cursor.close()
            connection.close()
