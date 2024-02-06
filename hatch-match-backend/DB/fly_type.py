from . import CURSOR, CONN

class Fly_type:

    all = {}

    def __init__(self, type, id = None):
        self.id = id
        self.type = type

    def __repr__(self):
       return f"{self.id}: {self.type}"

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of fly type instances """
        sql = """
            CREATE TABLE IF NOT EXISTS fly_types (
            type_id INTEGER PRIMARY KEY,
            type TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists fly type instances """
        sql = """
            DROP TABLE IF EXISTS fly_types;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        if self.id is None:
            sql = "INSERT INTO fly_types (type) VALUES (?)"
            CURSOR.execute(sql, (self.type,))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            sql = "UPDATE fly_types SET type = ? WHERE type_id = ?"
            CURSOR.execute(sql, (self.type, self.id))
            CONN.commit()

    def delete(self):
        if self.id is not None:
            sql = "DELETE FROM fly_types WHERE type_id = ?"
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
            self.id = None

    @classmethod
    def create(cls, type):
        """ Initialize a new Fly type instance and save the object to the database """
        fly = cls(type)
        fly.save()
        return fly

    
     
