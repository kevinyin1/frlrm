import webapp2
from __init__ import *
from search import Search

class MainPage(webapp2.RequestHandler):
    def get(self):
        render_template(self,'index.html')

app = webapp2.WSGIApplication([
    ('/search', Search),
    ('/', MainPage),
], debug=True)
