from __init__ import *
import webapp2

class Questionaire(webapp2.RequestHandler):
    def get(self):
        render_template(self, questionaire.html)