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
        self.receiver.create_view()


class ReadCommand(Command):
    def execute(self):
        self.receiver.read_view()


class UpdateCommand(Command):
    def execute(self):
        self.receiver.update_view()


class DeleteCommand(Command):
    def execute(self):
        self.receiver.delete_view()


class SearchCommand(Command):
    def execute(self):
        self.receiver.search_view()


class Controller:
    def __init__(self):
        self.facade = ImageFacade()

    def get_pics(self):
        return self.facade.get_all()

    def add_pic(self, path_to_pic):
        self.facade.add(name=os.path.basename(path_to_pic)[0], tags=Service.autotag(path_to_pic), path=path_to_pic)

    def update_name(self, idname, name):
        self.facade.update_name(idname, name)

    def update_tags(self, id, tags, ch):
        if ch == 1:
            self.facade.append_tags(id, tags)
        elif ch == 2:
            self.facade.update_tags(id, tags)
        else:
            Service.error()

    def search(self, request):
        return self.facade.get_image_bytag(request)

    def delete(self, id):
        self.facade.delete(id)
        # TODO: Add exception/check

    def id_input(self):
        id = input()
        if self.facade.get_image_byid(id):
            return id
        else:
            return Service.error()

    def create(self):
        self.add_pic(Service.path_input())


class Receiver:
    def __init__(self):
        self.controller = Controller()

    def create_view(self):
        template_renderer(context={}, template='add_pic.jinja2', cls=True)
        self.controller.create()

    def read_view(self):
        images = self.controller.get_pics()
        template_renderer(context={'images': images}, template='all_images.jinja2', cls=True)
        input("Для продолжения нажмите enter")

    def search_view(self):
        template_renderer(context={}, template='get_by_tag.jinja2', cls=True)
        resp = self.controller.search(input())
        if resp :
            template_renderer(context={'results': resp}, template='get_by_tag_2.jinja2', cls=True)
        else:
            print('Ничего не найдено')

    def update_view(self):
        self.update_tags_view(self.update_name_view())

    def update_name_view(self):
        template_renderer(context={}, template='update_pic_name.jinja2', cls=True)
        id = self.controller.id_input()
        template_renderer(context={}, template='update_pic_name_2.jinja2', cls=True)
        self.controller.update_name(id, input())
        return id

    def update_tags_view(self, id):
        template_renderer(context={}, template='update_pic_tags.jinja2', cls=True)
        ch = int(input())
        template_renderer(context={}, template='update_pic_tags2.jinja2', cls=True)
        newtag = input()
        self.controller.update_tags(id, newtag, ch)

    def delete_view(self):
        template_renderer(context={}, template='delete_pic.jinja2', cls=True)
        self.controller.delete(self.controller.id_input())

        # TODO: Add timestamp


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
    def path_input(cls):
        path = input()
        if os.path.exists(path):
            return path
        else:
            return Service.error()


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
