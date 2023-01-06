import os

from PIL import Image

STORAGE_URL = '../storage/'


class ImageModel:
    def __init__(self, url, name, tags):
        self.url = url
        self.name = name
        self.tags = tags
        self.img = Image.open(self.url)

    def save(self):
        self.img.save(STORAGE_URL + self.name)
        pass

    def delete(self):
        os.remove(STORAGE_URL + self.name)
        pass

    def get_by_tag(self):
        pass

    def set_tag(self):
        pass
