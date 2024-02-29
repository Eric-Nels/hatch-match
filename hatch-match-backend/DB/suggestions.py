from . import CURSOR, CONN
import base64

class Suggestions:

    all = {}

    def __init__(self, name, image, id=None):
        self.id = id
        self.name = name
        self.image = image

    def __repr__(self):
       return f"{self.id}: {self.name}"

    @classmethod
    def create_table(cls):
        """ Create a new table to persist fly suggestions """
        sql = """
            CREATE TABLE IF NOT EXISTS suggestions (
            id INTEGER PRIMARY KEY,
            name TEXT,
            image TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    