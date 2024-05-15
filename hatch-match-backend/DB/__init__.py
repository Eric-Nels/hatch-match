#!/usr/bin/env python3
import sqlite3

class DatabaseManager:
    def __init__(self, db_name='hatch-match.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()