import webapp2
from __init__ import *
from search import Search
from questionaire import Questionaire
class MainPage(webapp2.RequestHandler):
    def get(self):
        render_template(self,'index.html')

app = webapp2.WSGIApplication([
    ('/questionaire', Questionaire),
    ('/search', Search),
    ('/', MainPage),
], debug=True)
