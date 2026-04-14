from persistence.db import get_conecction

class Trip:

    def __init__(self, name: str, 
                 city:str,
                 latitude: float,
                 longitude: float
                 ):
        self.name = name
        self.city = city
        self.latitude = latitude
        self.longitude = longitude


    def getAll():
        try:
            connection = get_conecction()
            cursor = connection.cursor(dictionary = True)
            cursor.execute("SELECT id, name, city, latitude, longitude FROM trip")
            return cursor.fetchall()

        except Exception as ex:
            print(ex)
        
        finally:
            cursor.close()
            connection.close()