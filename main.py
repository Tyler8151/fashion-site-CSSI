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
User.query().fetch()



merchList = [
{'link': "/H&M", "id": "hm"},
{'link': "/Aeropostale", "id": "aero"},
{'link': '/AmericanEagle', 'id': 'AE'},
{'link': '/AmericanApparel', 'id': 'AA'},
{'link': '/Hollister', 'id': 'holl'},
{'link': '/BananaRepublic', 'id': 'banana'},
{'link': '/Bloomingdales', 'id': 'bloom'},
{'link': '/Express', 'id': 'exp'},
{'link': '/Forever21', 'id': 'f21'},
{'link': '/Gap', 'id': 'Gap'},
{'link': '/LuluLemon', 'id': 'Lulu'},
{'link': '/OldNavy', 'id': 'old'},
{'link': '/Uniqlo', 'id': 'Un'},
{'link': '/UrbanOutFitters', 'id': 'urb'},
{'link': '/Zara', 'id': 'zara'},
]


title_dict={'title': "", "desc": "",'opinion': "", 'logo': "", 'all_comments': comment_query, 'merchList': merchList, 'user': 'Sign in/Join' }



class MerchantPage(webapp2.RequestHandler):
    def __init__(self, title, description, opinion, logo, brand, clothing, image, request, response):
        merchList = [
        {'link': "/H&M", "id": "hm"},
        {'link': "/Aeropostale", "id": "aero"},
        {'link': '/AmericanEagle', 'id': 'AE'},
        {'link': '/AmericanApparel', 'id': 'AA'},
        {'link': '/Hollister', 'id': 'holl'},
        {'link': '/BananaRepublic', 'id': 'banana'},
        {'link': '/Bloomingdales', 'id': 'bloom'},
        {'link': '/Express', 'id': 'exp'},
        {'link': '/Forever21', 'id': 'f21'},
        {'link': '/Gap', 'id': 'Gap'},
        {'link': '/LuluLemon', 'id': 'Lulu'},
        {'link': '/OldNavy', 'id': 'old'},
        {'link': '/Uniqlo', 'id': 'Un'},
        {'link': '/UrbanOutFitters', 'id': 'urb'},
        {'link': '/Zara', 'id': 'zara'},
        ]
        self.title_dict ={'title': title, "desc": description, 'opinion': opinion, 'logo': logo, 'all_comments': comment_query, 'merchList': merchList, 'clothing': clothing, "image": image }
        self.brand = brand
        self.initialize(request, response)
    def get(self):
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(self.title_dict))

    def post(self):

        comment = self.request.get('comment')

        amerApparel_comment = Comment(user=user1.real_name, content=comment, brand=self.brand)
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

class UserHome(webapp2.RequestHandler):
    def get(self):
        user_dict = {
        'user': user1.real_name,
        }
        user_template = \
        log_template= jinja_current_directory.get_template('templates/homepg.html')
        self.response.write(log_template.render(user_dict))

class LogPage(webapp2.RequestHandler):
    def get(self):
        log_template= jinja_current_directory.get_template('templates/login-out.html')
        self.response.write(log_template.render())

    def post(self):
        user_name = self.request.get('username')
        password = self.request.get('password')

        #check that username and password are correct

        user_query = User.query().fetch()
        for user in user_query:
            print user
            if user_name == user.user_name and password == user.password:
                title_dict['user'] = 'Hello, %s!' % (user.real_name)
                return self.redirect('/')


        self.response.write('Unauthorized')








class AeroPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'Aeropostale',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/aeropostale.svg.png',\
        'Aeropostale',\
        "http://www.aeropostale.com/skinny-medium-wash-stretch-jean/64131354.html?dwvar_64131354_color=962&cgid=",\
        "http://www.aeropostale.com/dw/image/v2/BBSG_PRD/on/demandware.static/-/Sites-master-catalog-aeropostale/default/dwdffd5f1d/64131354_962_main.jpg?sw=2000&sh=2000&sm=fit&sfrm=jpg",\
         request, response)

class AmerEaglePage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'American Eagle',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/americaneagle.svg.png',\
        'American Eagle', request, response)

class AmerApparelPage(MerchantPage):
    def __init__(self, request, response):
        MerchantPage.__init__(self,\
        'American Apparel',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/americanapparel.png',\
        'American Apparel', request, response)

class BananaPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'Banana Republic',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/banana.png',\
        'Banana Republic', request, response)

class BloomPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'Bloomingdales',\
        "Although a bit on the pricier side, Bloomingdales expectations of quality apparel exceeds that of its many major competitors. Bloomingdales robust collection of jewelry, accessories, clothing, and handbags makes it a top retailer on many fashion enthusiasts radars. If your fashion standards only demand to be beaten, then Bloomingdales is your one-stop style shop.",\
        'This is where our opinion will go',\
        'images/bloom.png',\
        'Bloomingdales', request, response)

class ExpressPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'Express',\
        'Under CEO David Komberg, Express has expanded to encompass 641 factions as of January 2015. The catalog of clothing here mostly pertains to young women and men.',\
        'This is where our opinion will go',\
        'images/express.png',\
        'Express', request, response)

class F21Page(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'Forever 21',\
        'Forever 21 bravely embraces the quirkier and funkier nature of fashion while carefully treading the line between whats too weird and whats not. Those looking for a unique treat each visit to either their site or store will be pleasantly surprised to the plethora of tasteful accessories and apparel more so catered to young ladies.',\
        'This is where our opinion will go',\
        'images/f21.png',\
        'Forever 21', request, response)

class GapPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'Gap',\
        'Its headquarters located in San Fransisco, California, Gap is home to a wide variety of clothing. This all became possible through its co-founders Donald and Doris Fisher. Gap is home to many subsidiaries including Old Navy, Banana Republic and more.',\
        'This is where our opinion will go',\
        'images/gap.png',\
        'Gap', request, response)

class HMPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'H&M',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/hm-logo.png',\
        'H&M',\
        "http://www2.hm.com/en_us/productpage.0631735001.html",\
        "http://lp2.hm.com/hmgoepprod?set=source[/8a/5c/8a5c6a561d73203b2b0b8c6faf5018583a34ccb9.jpg],origin[dam],category[],type[DESCRIPTIVESTILLLIFE],hmver[1]&call=url[file:/product/style]",\
         request, response)

class HollPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'Hollister',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/hollister.png',\
        'Hollister', request, response)

class LuluPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'LuluLemon',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/lulu.png',\
        'LuluLemon', request, response)

class OldPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'Old Navy',\
        'Old Navy was originally named Gap Warehouse, but was later renamed to become a separate entity. It was then established in March of 1994, when it was named after a bar in Paris.',\
        'This is where our opinion will go',\
        'images/old.png',\
        'Old Navy', request, response)

class UnPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'Uniqlo',\
        'Uniqlo embraces the simplicity, longevity, and quality of Japanese values - and that is evident in their wide selection of affordable apparel. Enthusiasts familiar with popular clothing lines such as H&M or Forever 21 will feel right at home with Uniqlos unique approach to subtlety.',\
        'This is where our opinion will go',\
        'images/uni.png',\
        'Uniqlo', request, response)

class UrbPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'Urban OutFitters',\
        'Owned by Richard Hayne, urban outfitters headquarters is located in Philly, Pennsylvania. There are a total of 402 retail stores, and mostly selling what is known as "hipster clothing".',\
        'This is where our opinion will go',\
        'images/uni.png',\
        'Urban OutFitters', request, response)

class ZaraPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'Zara',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/zara.png',\
        'Zara', request, response)

class AboutPage(webapp2.RequestHandler):
    def get(self):
        home_template= jinja_current_directory.get_template('templates/about.html')
        self.response.write(home_template.render())
    def post(self):
        main_template= jinja_current_directory.get_template('templates/about.html')
        self.response.write(main_template.render())

class ConPage(webapp2.RequestHandler):
    def get(self):
        con_template= jinja_current_directory.get_template('templates/contact.html')
        print("getting conpage")
        self.response.write(con_template.render())

    def post(self):
        con_template= jinja_current_directory.get_template('templates/contact.html')
        print ("posting conpage")
        self.response.write(con_templaterender())

class RecPage(webapp2.RequestHandler):
    def get(self):
        rec_template= jinja_current_directory.get_template('templates/rec.html')
        self.response.write(rec_template.render())
    def post(self):
        rec_template= jinja_current_directory.get_template('templates/rec.html')
        self.response.write(rec_template.render())

class SignUpHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('name')
        username = self.request.get('username')
        email = self.request.get('email')
        password = self.request.get('password')

        user1 = User(user_name=username, real_name=name, email=email, password=password)

        user1.put()

        title_dict['user'] = 'Hello, %s!' % (user1.real_name)

        self.redirect('/')




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
    ('/contact',ConPage),
    ('/recommend', RecPage),
    ('/signup', SignUpHandler),
], debug=True)
