import os
import urllib
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def render_template(self, file_name, template_values={}):
    if not template_values:
        template_values = {}
    template = JINJA_ENVIRONMENT.get_template(file_name)
    self.response.write(template.render(template_values))
