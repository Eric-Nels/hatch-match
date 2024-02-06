from . import CURSOR, CONN

class Species:

    all = {}

    def __init__(self, name, image, id=None):
        self.id = id
        self.name = name
        self.image = image

    @staticmethod
    def create_table():
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS species (
                species_id INTEGER PRIMARY KEY,
                name TEXT,
                image TEXT
            )
        """)
        CONN.commit()

    @staticmethod
    def drop_table():
        CURSOR.execute("DROP TABLE IF EXISTS species")
        CONN.commit()

    def save(self):
        """ Insert a new row with the name of the current species instance.
        Update object id attribute using the primary key value of the new row
        """
        sql = """
            INSERT INTO species (name, image)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.image))
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, image):
        species = cls(name, image)
        species.save()
        return species