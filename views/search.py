import webapp2
from __init__ import *
from parser import *

class Search(webapp2.RequestHandler):
    def get(self):
        render_template(self, 'search.html')

    def post(self):
        start_destination = self.request.get('starting-destination')
        start_date = self.request.get('start-date')
        end_date = self.request.get('end-date')
        budget = self.request.get('budget')
        self._serve_page()

    def _serve_page(self):
        getDeals(self.request.get('start-date'), self.request.get('end-date'))
        template_values = {
            'start_destination': self.request.get('starting-destination'),
            'start_date': self.request.get('start-date'),
            'end_date': self.request.get('end-date'),
            'budget': self.request.get('budget'),
            'bestDeals': getBestDeals()
        }
        render_template(self, 'search.html', template_values)
