from . import CURSOR, CONN

class Flies:

    all = {}

    def __init__(self, name, image, type, imitation, life_cycle, id=None):
        self.id = id
        self.name = name
        self.image = image
        self.type = type
        self.imitation = imitation
        self.life_cycle = life_cycle


    def __repr__(self):
        return f"<Fly {self.id}: {self.name}, {self.type}, {self.imitation}, {self.life_cycle}"
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of fly instances """
        sql = """
            CREATE TABLE IF NOT EXISTS flies (
            fly_id INTEGER PRIMARY KEY,
            name TEXT,
            image TEXT,
            type TEXT,
            imitation TEXT,
            life_cycle TEXT
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
            INSERT INTO flies (name, image, type, imitation, life_cycle)
            VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.image, self.type, self.imitation, self.life_cycle))
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, image, type, imitation, life_cycle):
        """ Initialize a new Fly instance and save the object to the database """
        fly = cls(name, image, type, imitation, life_cycle)
        fly.save()
        return fly