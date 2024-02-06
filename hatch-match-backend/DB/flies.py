from . import CURSOR, CONN

class Flies:

    all = {}

    def __init__(self, name, image, type_id, species_id, id=None):
        self.id = id
        self.name = name
        self.image = image
        self.type_id = type_id
        self.species_id = species_id


    def __repr__(self):
        return f"<Fly {self.id}: {self.name}, {self.type_id}"
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of fly instances """
        sql = """
            CREATE TABLE IF NOT EXISTS flies (
            id INTEGER PRIMARY KEY,
            name TEXT,
            image TEXT,
            type_id INTEGER,
            species_id INTEGER,
            FOREIGN KEY (type_id) REFERENCES fly_type(type_id),
            FOREIGN KEY (species_id) REFERENCES species(species_id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists fly instances """
        sql = """
            DROP TABLE IF EXISTS flies;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name of the current fly instance.
        Update object id attribute using the primary key value of the new row
        """
        sql = """
            INSERT INTO flies (name, image, type_id, species_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.image, self.type_id, self.species_id))
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, image, type_id, species_id):
        """ Initialize a new Fly instance and save the object to the database """
        fly = cls(name, image, type_id, species_id)
        fly.save()
        return fly