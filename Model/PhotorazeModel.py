import os
import sqlite3
from PIL import Image

STORAGE_URL = '../storage/'

class ImageModel:
    def __init__(self, url, name, tags):
        self.url = url
        self.name = name
        self.tags = tags
        self.img = Image.open(self.url)

        self.conn = sqlite3.connect("../db_phr")
        self.cursor = self.conn.cursor()

    def save(self):
        self.img.save(STORAGE_URL + self.name)
        sql = """ INSERT INTO images(name, tags) VALUES(
                ?, ?)
                """
        self.cursor.execute(sql, (str(self.name), " ".join(self.tags)))
        self.conn.commit()
        pass

    def delete(self):
        os.remove(STORAGE_URL + self.name)
        sql = """
            DELETE FROM images WHERE name=?
        """
        self.cursor.execute(sql, (str(self.name), ))
        self.conn.commit()
        pass

    def update(self, utags):
        sql = """
            UPDATE images
            SET tags = ?
            WHERE name = ? 
        """
        self.cursor.execute(sql, (utags, self.name))
        self.conn.commit()
        pass

    def read(self):
        sql = """
                SELECT tags FROM images WHERE name = ?
        """
        self.cursor.execute(sql, (self.name,))
        self.conn.commit()
        records = self.cursor.fetchall()
        return records


