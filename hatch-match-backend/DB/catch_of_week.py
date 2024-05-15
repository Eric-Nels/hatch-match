from . import DatabaseManager
import base64

class Catch_of_week:

    def __init__(self, catch_image, social, id=None):
        self.id = id
        self.catch_image = catch_image
        self.social = social

    def __repr__(self):
        return f"<Catch {self.id}: {self.catch_image}, {self.social}>"
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of a catch of the week submition """
        with DatabaseManager() as cursor:
            sql = """
                CREATE TABLE IF NOT EXISTS catch_of_week (
                id INTEGER PRIMARY KEY,
                catch_image TEXT,
                social TEXT
                )
            """
            cursor.execute(sql) 

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists catch of the week submition """
        with DatabaseManager() as cursor:
            sql = """
                DROP TABLE IF EXISTS catch_of_week;
            """
            cursor.execute(sql)       

    def save(self):
        """ Insert a new row with the name of the current catch of the week submition.
        Update object id attribute using the primary key value of the new row
        """
        with DatabaseManager() as cursor:
            encoded_catch_image = base64.b64encode(self.catch_image).decode('utf-8')
            sql = """
                INSERT INTO catch_of_week (catch_image, social)
                VALUES (?, ?)
            """
            cursor.execute(sql, (encoded_catch_image, self.social))
            self.id = cursor.lastrowid