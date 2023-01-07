from Model.PhotorazeModel import ImageModel
import os

URL = '../images/1.jpg'


# img.save()
# img.delete()
# img.update('test tes test st st')

class ImageController:
    def __init__(self, view):
        self.view = view
        self.model = ImageModel

    def upload_image(self, url, tags):
        name = os.basename(url)
        img = self.model(url, name, tags)
        img.save()
