import jinja2
import os
import webapp2
from models import User

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

title_dict={'title': "test"}

class HomePage(webapp2.RequestHandler):
    def get(self):
        main_template= jinja_current_directory.get_template('templates/homepg.html')
        self.response.write(main_template.render(title_dict))

    def post(self):
        main_template= jinja_current_directory.get_template('templates/homepg.html')
        self.response.write(main_template.render(title_dict))

class LogPage(webapp2.RequestHandler):
    def post(self):
        log_template= jinja_current_directory.get_template('templates/login-out.html')
        self.response.write(log_template.render())

class AeroPage(webapp2.RequestHandler):
    def post(self):
        title_dict['title']='Aeropostale'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
class AmerEaglePage(webapp2.RequestHandler):
    def post(self):
        title_dict['title']='American Eagle'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
class AmerApparelPage(webapp2.RequestHandler):
    def post(self):
        title_dict['title']='American Apparel'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
class BananaPage(webapp2.RequestHandler):
    def post(self):
        title_dict['title']='Banana Republic'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
class BloomPage(webapp2.RequestHandler):
    def post(self):
        title_dict['title']='Bloomingdales'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
class ExpressPage(webapp2.RequestHandler):
    def post(self):
        title_dict['title']='Express'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
class F21Page(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='Forever 21'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
class GapPage(webapp2.RequestHandler):
    def post(self):
        title_dict['title']='Gap'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
class HMPage(webapp2.RequestHandler):
    def post(self):
        title_dict['title']='H&M'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
class HollPage(webapp2.RequestHandler):
    def post(self):
        title_dict['title']='Hollister'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
class LuluPage(webapp2.RequestHandler):
    def post(self):
        title_dict['title']='LuluLemon'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
class OldPage(webapp2.RequestHandler):
    def post(self):
        title_dict['title']='Old Navy'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
class UnPage(webapp2.RequestHandler):
    def post(self):
        title_dict['title']='Uniqlo'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
class UrbPage(webapp2.RequestHandler):
    def post(self):
        title_dict['title']='Urban Outfitters'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
class ZaraPage(webapp2.RequestHandler):
    def post(self):
        title_dict['title']='Zara'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))



app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/log',LogPage),
    ('/Aeropostale',AeroPage),
    ('/AmericanEagle',AmerEaglePage),
    ('/AmericanApparel',AmerApparelPage),
    ('/BananaRepublic',BananaPage),
    ('/Bloomingdales',BloomPage),
    ('/Express',ExpressPage),
    ('/Forever21',F21Page),
    ('/Gap',GapPage),
    ('/H&M',HMPage),
    ('/Hollister',HollPage),
    ('LuluLemon',LuluPage),
    ('/OldNavy',OldPage),
    ('/Uniqlo',UnPage),
    ('/UrbanOutFitters',UrbPage),
    ('/Zara',ZaraPage)
], debug=True)
