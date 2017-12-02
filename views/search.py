import webapp2
from __init__ import *

class Search(webapp2.RequestHandler):
    def get(self):
        render_template(self, 'mapstart.html')
