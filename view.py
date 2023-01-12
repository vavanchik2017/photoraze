import os

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader(__name__, "templates"),
    autoescape=select_autoescape("html", "xml")
)


def clean_screen(flag):
    if flag:
        os.system('cls' if os.name == 'nt' else 'clear')


def template_renderer(context=None, template='default.jinja2', cls=True):
    if not context:
        context = {}
    clean_screen(cls)
    template = env.get_template(template)
    print(template.render(**context))
