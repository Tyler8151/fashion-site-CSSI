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
        home_template= jinja_current_directory.get_template('homepg/welcome.html')
        self.response.write(home_template.render())






app = webapp2.WSGIApplication([
    ('/', HomePage)
], debug=True)