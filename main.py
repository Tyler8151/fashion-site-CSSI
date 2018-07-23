import jinja2
import os
import webapp2
from models import User

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

title_dict={'title': "", "desc": "",'opinion': "", 'logo': "" }

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
    def get(self):
        title_dict['logo']='/images/aeropostale.svg.png'
        title_dict['title']='Aeropostale'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
    def post(self):
        title_dict['title']='Aeropostale'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='/images/aeropostale.svg.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class AmerEaglePage(webapp2.RequestHandler):
    def get(self):
        title_dict['logo']='images/americaneagle.svg.png'
        title_dict['title']='American Eagle'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
    def post(self):
        title_dict['title']='American Eagle'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/americaneagle.svg.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class AmerApparelPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='American Apparel'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/americanapparel.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
    def post(self):
        title_dict['title']='American Apparel'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/americanapparel.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class BananaPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='Banana Republic'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/banana.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
    def post(self):
        title_dict['title']='Banana Republic'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/banana.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class BloomPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='Bloomingdales'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/bloom.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
    def post(self):
        title_dict['title']='Bloomingdales'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/bloom.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class ExpressPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='Express'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/express.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
    def post(self):
        title_dict['title']='Express'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/express.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class F21Page(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='Forever 21'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/f21.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
    def post(self):
        title_dict['title']='Forever 21'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/f21.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class GapPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='Gap'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/gap.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
    def post(self):
        title_dict['title']='Gap'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/gap.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class HMPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='H&M'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/hm-logo.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
    def post(self):
        title_dict['title']='H&M'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/hm-logo.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class HollPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='Hollister'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/hollister.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
    def post(self):
        title_dict['title']='Hollister'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/hollister.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class LuluPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='LuluLemon'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/lulu.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
    def post(self):
        title_dict['title']='LuluLemon'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/lulu.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class OldPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='Old Navy'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/old.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
    def post(self):
        title_dict['title']='Old Navy'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/old.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class UnPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='Uniqlo'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/uni.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
    def post(self):
        title_dict['title']='Uniqlo'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/uni.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class UrbPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='Urban Outfitters'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/urb.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
    def post(self):
        title_dict['title']='Urban Outfitters'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/urb.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class ZaraPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='Zara'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/zara.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
    def post(self):
        title_dict['title']='Zara'
        title_dict['desc']='This part of the webiste will contain the description of the brand'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/zara.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class AboutPage(webapp2.RequestHandler):
    def post(self):
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render())

class ConPage(webapp2.RequestHandler):
    def get(self):
        con_template= jinja_current_directory.get_template('templates/contact.html')
        self.response.write(con_template.render())



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
    ('/LuluLemon',LuluPage),
    ('/OldNavy',OldPage),
    ('/Uniqlo',UnPage),
    ('/UrbanOutFitters',UrbPage),
    ('/Zara',ZaraPage),
    ('/about',AboutPage),
    ('/contact',ConPage)
], debug=True)
