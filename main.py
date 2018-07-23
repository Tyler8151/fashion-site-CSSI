import jinja2
import os
import webapp2
from models import User

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)



class HomePage(webapp2.RequestHandler):
    def get(self):
        home_template= jinja_current_directory.get_template('templates/homepg.html')
        self.response.write(home_template.render())


class LogPage(webapp2.RequestHandler):
    def post(self):
        log= jinja_current_directory.get_template('templates/log-out.html')
        self.response.write(home_template.render())






app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/log',LogPage),
    ('/h&m',HMPage),
    ('/aero',AeroPage),
    ('/AmericanEagle',AmerEaglePage),
    ('/AmericanApparel',AmerApparelPage),
    ('/BananaRepublic',BananaPage),
    ('/Bloomingdales'BloomPage),
    ('/Express',ExpressPage),
    ('/Forever21',F21Page),
    ('/Gap',GapPage),
    ('/H')
], debug=True)
