#from os.path import join
from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def render(template_name, folder='templates', **kwargs):
    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)
    return template.render(**kwargs)

    #file_path = join(folder, template_name)
    #with open(file_path, encoding='utf-8') as f:
        #return Template(f.read()).render(**kwargs)
