import webapp2
from __init__ import *

class MainPage(webapp2.RequestHandler):
    def get(self):
        render_template(self,'index.html')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
