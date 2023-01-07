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
        self.cursor.execute(""" INSERT INTO images(name, tags) VALUES(
                .format(self.name),.format(self.tags))
                """)
        self.conn.commit()
        pass

    def delete(self):
        os.remove(STORAGE_URL + self.name)
        pass

    def get_by_tag(self):
        pass

    def set_tag(self):
        pass
