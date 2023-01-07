from Controller.PhotorazeController import ImageController
import fire


class ImageView:
    def __init__(self):
        self.controller = ImageController

    def addpic(self, url, tags):
        tags = 'person'
        self.controller.upload_image(url, tags)
        pass

    def change_tags(name):
        pass

    def change_name(name):
        pass

    def search(request):
        pass

    def delete(name):
        pass


def help():
    print('Test')


if __name__ == '__main__':
    fire.Fire(ImageView)
