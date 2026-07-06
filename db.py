import psycopg2
from psycopg2.extras import RealDictCursor

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="inventario",
            user="postgres",
            password="12345"
        )
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)

    def execute(self, query, params=None):
        self.cursor.execute(query, params)

        if self.cursor.description:
            return self.cursor.fetchall()
            
        self.conn.commit()
        return None

    def close(self):
        self.cursor.close()
        self.conn.close()
