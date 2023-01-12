import os.path
import tempfile
import subprocess
from view import template_renderer
import shutil
from model import Image
from os import path
#TODO: MAKE OOP!
#TODO: Merge templates
STORAGE = './storage/'


def default_controller(data=None, cls=True):
    template_renderer(context={}, template='default.jinja2', cls=cls)
    return (input(), None)


def exit_controller(data=None, cls=True):
    template_renderer(context={}, template='exit.jinja2', cls=cls)
    exit()


def add_pic(data=None, cls=True):
    template_renderer(context={}, template='add_pic.jinja2', cls=cls)
    imgpath = input()
    if os.path.exists(imgpath):
        new_location = shutil.copy(imgpath, STORAGE)
    return 11, new_location
    # TODO: Add exception


def add_pic_name(data=None, cls=True):
    template_renderer(context={}, template='add_pic_name.jinja2', cls=cls)
    imgname = input()
    return '11', imgname
    # TODO: Add timestamp to name


def add_pic_tags(imgname, cls=True):
    print(imgname)
    template_renderer(context={}, template='add_pic_tags.jinja2', cls=cls)
    tags = input()
    img = Image.add(name=imgname, tags=tags)
    return 51, img


def delete_pic(data=None, cls=True):
    template_renderer(context={}, template='delete_pic.jinja2', cls=cls)
    pic_to_del = input()
    Image.delete(pic_to_del)
    return 51, None
    # TODO: Add exception


def get_all_pics(data=None, cls=True):
    images = Image.get_all()
    print(images)
    template_renderer(context={'images': images}, template='all_images.jinja2', cls=cls)
    input("Продолжить?")
    return 'main', None  # (next state, data)


def update_pic_name(data=None, cls=True):
    template_renderer(context={}, template='update_pic_name.jinja2', cls=cls)
    id = input()
    template_renderer(context={}, template='update_pic_name_2.jinja2', cls=cls)
    new_name = input()
    Image.update_name(id, new_name)
    # TODO: Add timestamp
    return 'main', None


def update_pic_tags(data=None, cls=True):
    template_renderer(context={}, template='update_pic_tags.jinja2', cls=cls)
    id_tag = int(input())
    template_renderer(context={}, template='update_pic_tags2.jinja2', cls=cls)
    new_tags = Image.get_tags(id_tag)
    edited_tags = edit_tags(new_tags)
    Image.update_tags(id_tag, edited_tags)
    return 'main', None
    # TODO: Edit source text in terminal
    # TODO: Get value from tags


def get_by_tag(data=None, cls=True):
    template_renderer(context={}, template='get_by_tag.jinja2', cls=cls)
    request = input()
    tags = Image.get_image_bytag(request)
    template_renderer(context={'results': tags}, template='get_by_tag_2.jinja2', cls=cls)
    return 'main', None


def get_controller(state):
    return func_dict.get(state, default_controller)


def autotag(imgpath):
    pass
    # TODO: Send image to get tags from neuralink


def get_tags_neuro(tags):
    pass
    # TODO: Get new tags for pic. Replace tag if matched


def edit_tags(tags):
    tmp = tempfile.NamedTemporaryFile(delete=False)
    try:
        editor = os.environ['EDITOR']
    except:
        editor = 'nano'
    f = open(tmp.name,'r+')
    f.seek(0)
    f.write(tags)
    subprocess.call([editor, tmp.name])
    updated_tags = f.read()
    f.close()
    print(updated_tags)
    return updated_tags


func_dict = {
    '0': exit_controller,
    '1': add_pic,
    '2': delete_pic,
    '3': get_all_pics,
    '4': update_pic_name,
    '5': update_pic_tags,
    '6': get_by_tag,
    '11': add_pic_tags
}
