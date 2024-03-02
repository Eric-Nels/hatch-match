from . import DatabaseManager
import base64

class Suggestions:
    def __init__(self, name, imitation, life_cycle, image, id=None):
        self.id = id
        self.name = name
        self.imitation = imitation
        self.life_cycle = life_cycle
        self.image = image

    def __repr__(self):
        return f"{self.id}: {self.name} {self.imitation} {self.life_cycle}"

    @classmethod
    def create_table(cls):
        """ Create a new table to persist fly suggestions """
        with DatabaseManager() as cursor:
            sql = """
                CREATE TABLE IF NOT EXISTS suggestions (
                id INTEGER PRIMARY KEY,
                name TEXT,
                imitation TEXT,
                life_cycle TEXT,
                image TEXT)
            """
            cursor.execute(sql)

    @classmethod
    def drop_table(cls):
        """ Drop the suggestions table if it exists """
        with DatabaseManager() as cursor:
            sql = "DROP TABLE IF EXISTS suggestions"
            cursor.execute(sql)

    def save(self):
        """Save the suggestion to the database"""
        with DatabaseManager() as cursor:
            # Encode the image data as base64
            encoded_image = base64.b64encode(self.image).decode('utf-8')
            sql = "INSERT INTO suggestions (name, imitation, life_cycle, image) VALUES (?, ?, ?, ?)"
            cursor.execute(sql, (self.name, self.imitation, self.life_cycle, encoded_image))
    