from . import DatabaseManager

class Bugs:
    def __init__(self, name, life_cycle, image, id=None):
        self.id = id
        self.name = name
        self.life_cycle = life_cycle
        self.image = image

    def __repr__(self):
        return f"<{self.id}: {self.name}, {self.life_cycle}>"

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of bug instances """
        with DatabaseManager() as cursor:
            sql = """
                CREATE TABLE IF NOT EXISTS bugs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                life_cycle TEXT,
                image TEXT
                )
            """
            cursor.execute(sql)

    @classmethod
    def drop_table(cls):
        """ Drops the table that persists bug instances """ 
        with DatabaseManager() as cursor:
            sql = """
                DROP TABLE IF EXISTS bugs;
            """
            cursor.execute(sql)

    def save(self):
        """ Insert a new row with the name of the current bug instance.
        Update object id attribute using the primary key value of the new row
        """
        with DatabaseManager() as cursor:
            sql = """
                INSERT INTO bugs (name, life_cycle, image)
                VALUES (?, ?, ?)
            """
            cursor.execute(sql, (self.name, self.life_cycle, self.image))
            self.id = cursor.lastrowid

    @classmethod
    def create(cls, name, life_cycle, image):
        """ Initialize a new bug instance and save the object to the database """
        bug = cls(name, life_cycle, image)
        bug.save()
        return bug