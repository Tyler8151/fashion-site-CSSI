import jinja2
import os
import webapp2
from models import User
from models import Comment

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

comment_query = Comment.query().fetch()

title_dict={'title': "", "desc": "",'opinion': "", 'logo': "", 'all_comments': comment_query }

merchList = [
{"link": "/H&M", "id": "hm"},
{"link": "/Aeropostale", "id": "aero"}

]

class MerchantPage(webapp2.RequestHandler):
    def __init__(self, title, description, opinion, logo, brand, request, response):
        self.title_dict ={'title': title, "desc": description, 'opinion': opinion, 'logo': logo, 'all_comments': comment_query }
        self.brand = brand
        self.initialize(request, response)
    def get(self):
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(self.title_dict))

    def post(self):

        comment = self.request.get('comment')
        print '\n\n\n\n\n\nhey\n\n'
        print comment
        print '*******************\n'

        amerApparel_comment = Comment(content=comment, brand=self.brand)
        amerApparel_comment.put()

        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(self.title_dict))

class HomePage(webapp2.RequestHandler):
    def get(self):
        main_template= jinja_current_directory.get_template('templates/homepg.html')
        self.response.write(main_template.render(title_dict))

    def post(self):
        main_template= jinja_current_directory.get_template('templates/homepg.html')
        self.response.write(main_template.render(title_dict))

class LogPage(webapp2.RequestHandler):
    def get(self):
        log_template= jinja_current_directory.get_template('templates/login-out.html')
        self.response.write(log_template.render())

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

        comment = self.request.get('comment')

        aero_comment = Comment(content=comment, brand='Aeropostale')
        aero_comment.put()

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

        comment = self.request.get('comment')

        amerEagle_comment = Comment(content=comment, brand='American Eagle')
        amerEagle_comment.put()

        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

# class AmerApparelPage(webapp2.RequestHandler):
#     def get(self):
#         title_dict['title']='American Apparel'
#         title_dict['desc']='American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.'
#         title_dict['opinion']='This is where our opinion will go'
#         title_dict['logo']='images/americanapparel.png'
#         home_template= jinja_current_directory.get_template('templates/store.html')
#         self.response.write(home_template.render(title_dict))
#
#     def post(self):
#         title_dict['title']='American Apparel'
#         title_dict['desc']='American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.'
#         title_dict['opinion']='This is where our opinion will go'
#         title_dict['logo']='images/americanapparel.png'
#
#         comment = self.request.get('comment')
#
#         amerApparel_comment = Comment(content=comment, brand='American Apparel')
#         amerApparel_comment.put()
#
#         home_template= jinja_current_directory.get_template('templates/store.html')
#         self.response.write(home_template.render(title_dict))
class AmerApparelPage(MerchantPage):
    def __init__(self, request, response):
        MerchantPage.__init__(self,\
         'American Apparel',\
          'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
           'This is where our opinion will go',\
          'images/americanapparel.png',\
          'American Apparel', request, response)
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

        comment = self.request.get('comment')

        banana_comment = Comment(content=comment, brand='Banana Republic')
        banana_comment.put()

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

        comment = self.request.get('comment')

        bloom_comment = Comment(content=comment, brand='Bloomingdales')
        bloom_comment.put()

        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class ExpressPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='Express'
        title_dict['desc']='Under CEO David Komberg, Express has expanded to encompass 641 factions as of January 2015. The catalog of clothing here mostly pertains to young women and men.'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/express.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

    def post(self):
        title_dict['title']='Express'
        title_dict['desc']='Under CEO David Komberg, Express has expanded to encompass 641 factions as of January 2015. The catalog of clothing here mostly pertains to young women and men.'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/express.png'

        comment = self.request.get('comment')

        exp_comment = Comment(content=comment, brand='Express')
        exp_comment.put()

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

        comment = self.request.get('comment')

        f21_comment = Comment(content=comment, brand='Forever 21')
        f21_comment.put()

        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class GapPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='Gap'
        title_dict['desc']='Its headquarters located in San Fransisco, California, Gap is home to a wide variety of clothing. This all became possible through its co-founders Donald and Doris Fisher. Gap is home to many subsidiaries including Old Navy, Banana Republic and more.'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/gap.png'

        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))
        
    def post(self):
        title_dict['title']='Gap'
        title_dict['desc']='Its headquarters located in San Fransisco, California, Gap is home to a wide variety of clothing. This all became possible through its co-founders Donald and Doris Fisher. Gap is home to many subsidiaries including Old Navy, Banana Republic and more.'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/gap.png'

        comment = self.request.get('comment')

        gap_comment = Comment(content=comment, brand='Gap')
        gap_comment.put()

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

        comment = self.request.get('comment')

        hm_comment = Comment(content=comment, brand='H&M')
        hm_comment.put()

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

        comment = self.request.get('comment')

        holl_comment = Comment(content=comment, brand='Hollister')
        holl_comment.put()

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

        comment = self.request.get('comment')

        lulu_comment = Comment(content=comment, brand='LuluLemon')
        lulu_comment.put()

        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class OldPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='Old Navy'
        title_dict['desc']='Old Navy was originally named Gap Warehouse, but was later renamed to become a separate entity. It was then established in March of 1994, when it was named after a bar in Paris.'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/old.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

    def post(self):
        title_dict['title']='Old Navy'
        title_dict['desc']='Old Navy was originally named Gap Warehouse, but was later renamed to become a separate entity. It was then established in March of 1994, when it was named after a bar in Paris.'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/old.png'

        comment = self.request.get('comment')

        old_comment = Comment(content=comment, brand='Old Navy')
        old_comment.put()

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

        comment = self.request.get('comment')

        uni_comment = Comment(content=comment, brand='Uniqlo')
        uni_comment.put()

        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class UrbPage(webapp2.RequestHandler):
    def get(self):
        title_dict['title']='Urban Outfitters'
        title_dict['desc']='Owned by Richard Hayne, urban outfitters headquarters is located in Philly, Pennsylvania. There are a total of 402 retail stores, and mostly selling what is known as "hipster clothing".'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/urb.png'
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

    def post(self):
        title_dict['title']='Urban Outfitters'
        title_dict['desc']='Owned by Richard Hayne, urban outfitters headquarters is located in Philly, Pennsylvania. There are a total of 402 retail stores, and mostly selling what is known as "hipster clothing".'
        title_dict['opinion']='This is where our opinion will go'
        title_dict['logo']='images/urb.png'

        comment = self.request.get('comment')

        urb_comment = Comment(content=comment, brand='Urban Outfitters')
        urb_comment.put()

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

        comment = self.request.get('comment')


        zara_comment = Comment(content=comment, brand='Zara')
        zara_comment.put()

        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(title_dict))

class AboutPage(webapp2.RequestHandler):
    def get(self):
        home_template= jinja_current_directory.get_template('templates/about.html')
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
