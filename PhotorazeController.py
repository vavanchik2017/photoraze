from abc import ABC, abstractmethod
from PhotorazeView import template_renderer
from PhotorazeModel import ImageFacade
from autotag import VGG
import os.path
import shutil


STORAGE = './storage/'


class Command(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class CreateCommand(Command):
    def execute(self):
        self.receiver.create()


class ReadCommand(Command):
    def execute(self):
        self.receiver.read()


class UpdateCommand(Command):
    def execute(self):
        self.receiver.update()


class DeleteCommand(Command):
    def execute(self):
        self.receiver.delete()


class SearchCommand(Command):
    def execute(self):
        self.receiver.search()


class Receiver:
    def __init__(self):
        self.facade = ImageFacade()
    def add_pic_tags(self, imgname, cls=True):
        template_renderer(context={}, template='add_pic_tags.jinja2', cls=cls)
        tags = Service.autotag(imgname)
        self.facade.add(name=os.path.basename(imgname)[0], tags=tags, path=imgname)
        return 'ok'


    def create_view(self):
        template_renderer(context={}, template='add_pic.jinja2', cls=True)
        self.create()

    def create(self):
        imgpath = input()
        if os.path.exists(imgpath):
            self.add_pic_tags(Service.copy(imgpath))
        else:
            return Service.error()

    def read(self):
        images = self.facade.get_all()
        print(images)
        template_renderer(context={'images': images}, template='all_images.jinja2', cls=True)
        input("Для продолжения нажмите enter")


    def search_view(self):
        template_renderer(context={}, template='get_by_tag.jinja2', cls=True)
        if self.search():
            template_renderer(context={'results': self.search()}, template='get_by_tag_2.jinja2', cls=True)
        else:
            print('Ничего не найдено')

    def search(self):
        return self.facade.get_image_bytag(input())

    def update_name(self):
        template_renderer(context={}, template='update_pic_name.jinja2', cls=True)
        id = self.idInput()
        template_renderer(context={}, template='update_pic_name_2.jinja2', cls=True)
        self.facade.update_name(id, self.nameInput())
    def update_tags(self,id):
        template_renderer(context={}, template='update_pic_tags.jinja2', cls=True)
        ch = int(input())
        template_renderer(context={}, template='update_pic_tags2.jinja2', cls=True)
        newtag = input()
        if ch == 1:
            self.facade.append_tags(id, newtag)
        elif ch == 2:
            self.facade.update_tags(id, newtag)
        else:
            pass

    def idInput(self):
        if self.facade.get_image_byid(input()):
            return id
        else:
            return Service.error()
    def nameInput(self):
        return input()

        # TODO: Add timestamp

    def delete(self):
        self.facade.delete(self.idInput())
        # TODO: Add exception/check



class Menu:
    def __init__(self):
        self.commands = {}
        self.receiver = Receiver()

    def add_command(self, command_name, command):
        self.commands[command_name] = command

    def execute_command(self, command_name):
        self.commands[command_name].execute()


class Service:
    @classmethod
    def copy(cls, img):
        new_location = shutil.copy(img, STORAGE)
        return new_location
    @classmethod
    def error(cls):
        template_renderer(context={}, template='error.jinja2', cls=cls)
        return None

    @classmethod
    def autotag(cls, imgpath):
        at = VGG()
        return at.gettag(imgpath)

    @classmethod
    def choise(cls):
        pass

# TODO: Доделать апдейт

# TODO: Перечисление предложенных тегов для пользователя
