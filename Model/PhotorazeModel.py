STORAGE_URL = '/storage'


class Image:
    def __init__(self, url, name, tags):
        self.url = url
        self.name = name
        self.tags = tags

    def save(self):
        pass
    def get_by_tag(self):
        pass
    def set_tag(self):
        pass
    def delete(self):
        pass
