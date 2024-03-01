from . import DatabaseManager

class Flies:
    def __init__(self, name, image, type, imitation, life_cycle, id=None):
        self.id = id
        self.name = name
        self.image = image
        self.type = type
        self.imitation = imitation
        self.life_cycle = life_cycle

    def __repr__(self):
        return f"<Fly {self.id}: {self.name}, {self.type}, {self.imitation}, {self.life_cycle}>"

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of fly instances """
        with DatabaseManager() as cursor:
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
            cursor.execute(sql)

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists fly instances """
        with DatabaseManager() as cursor:
            sql = """
                DROP TABLE IF EXISTS flies;
            """
            cursor.execute(sql)

    def save(self):
        """ Insert a new row with the name of the current fly instance.
        Update object id attribute using the primary key value of the new row
        """
        with DatabaseManager() as cursor:
            sql = """
                INSERT INTO flies (name, image, type, imitation, life_cycle)
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (self.name, self.image, self.type, self.imitation, self.life_cycle))
            self.id = cursor.lastrowid

    @classmethod
    def create(cls, name, image, type, imitation, life_cycle):
        """ Initialize a new Fly instance and save the object to the database """
        fly = cls(name, image, type, imitation, life_cycle)
        fly.save()
        return fly