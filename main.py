import jinja2
import os
import webapp2
from models import User
from models import Comment
from google.appengine.api import users
from time import sleep

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)
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

homepage_data={'merchList': merchList, 'user': 'Sign in/Join', 'logout': '' }

User.query().fetch()








class MerchantPage(webapp2.RequestHandler):

    def __init__(self, title, description, opinion, logo, brand, clothing, image, request, response):

        self.title_dict ={'title': title, "desc": description, 'opinion': opinion, 'logo': logo, 'clothing': clothing, "image": image }

    def __init__(self, title, description, opinion, logo, brand, clothing, image, clothing2, image2, clothing3, image3, request, response):
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
        self.title_dict ={'title': title, "desc": description, 'opinion': opinion, 'logo': logo, 'all_comments': Comment.query().fetch(), 'merchList': merchList, 'clothing': clothing, "image": image, 'clothing2': clothing2, 'image2': image2, 'clothing3': clothing3, "image3": image3}

        self.brand = brand
        self.initialize(request, response)
    def get(self):

        self.title_dict['comments'] = Comment.query().filter(Comment.brand == self.brand).fetch()
        home_template= jinja_current_directory.get_template('templates/store.html')
        self.response.write(home_template.render(self.title_dict))

    def post(self):


        comment = self.request.get('comment')
        name = self.request.get('name')
        username = self.request.get('username')
        email = self.request.get('email')
        password = self.request.get('password')

        user1 = User(user_name=username, real_name=name, email=email, password=password)

        amerApparel_comment = Comment(user=user1.real_name, content=comment, brand=self.brand)
        amerApparel_comment.put()

        sleep(1)

        self.get()

class HomePage(webapp2.RequestHandler):
    def get(self):

        main_template= jinja_current_directory.get_template('templates/homepg.html')
        self.response.write(main_template.render(homepage_data))

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
                homepage_data['user'] = 'Hello, %s!' % (user.real_name)
                homepage_data['logout'] = 'Log out'
                return self.redirect('/')


        self.response.write('Unauthorized')








class AeroPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'A E R O P O S T A L E',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/aeropostale.svg.png',\
        'Aeropostale',\
        "http://www.aeropostale.com/skinny-medium-wash-stretch-jean/64131354.html?dwvar_64131354_color=962&cgid=",\
        "http://www.aeropostale.com/dw/image/v2/BBSG_PRD/on/demandware.static/-/Sites-master-catalog-aeropostale/default/dwdffd5f1d/64131354_962_main.jpg?sw=2000&sh=2000&sm=fit&sfrm=jpg",\
        "http://www.aeropostale.com/twill-midi-shorts/85133626.html?dwvar_85133626_color=102&cgid=girls-bottoms-shorts#content=HP_aSpot&start=2",\
        "http://www.aeropostale.com/dw/image/v2/BBSG_PRD/on/demandware.static/-/Sites-master-catalog-aeropostale/default/dw03c39ae5/85133626_102_main.jpg?sw=2000&sh=2000&sm=fit&sfrm=jpg",\
        "http://www.aeropostale.com/free-state-japanese-girl-power-graphic-tee/80104358.html?dwvar_80104358_color=102&cgid=girls-tops-graphictees#start=4",\
        "http://www.aeropostale.com/dw/image/v2/BBSG_PRD/on/demandware.static/-/Sites-master-catalog-aeropostale/default/dw86c73a8d/80104358_102_main.jpg?sw=2000&sh=2000&sm=fit&sfrm=jpg",\
        request, response)

class AmerEaglePage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'A M E R I C A N - E A G L E',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/americaneagle.svg.png',\
        'American Eagle',\
        "https://www.ae.com/women-aeo-velvet-double-strap-sandal-mustard/web/s-prod/1415_4051_284?cm=sUS-cUSD&catId=cat7900075",\
        "https://s7d2.scene7.com/is/image/aeo/1415_4051_284_f?$PDP_78_Main$",\
        "https://www.ae.com/women-ae-smocked-crop-top-navy/web/s-prod/2352_9283_410?cm=sUS-cUSD&catId=cat8420021",\
        "https://s7d2.scene7.com/is/image/aeo/2352_9283_410_of?$PDP_78_Main$",\
        "https://www.ae.com/men-jeans-ae-flex-skinny-jean-dark-rinse/web/s-prod/0119_4598_534?cm=sUS-cUSD&catId=cat6430041",\
        "https://s7d2.scene7.com/is/image/aeo/0119_4598_534_of?$PDP_78_Main$",\
         request, response)

class AmerApparelPage(MerchantPage):
    def __init__(self, request, response):
        MerchantPage.__init__(self,\
        'A M E R I C A N - A P P A R E L',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/americanapparel.png',\
        'American Apparel',\
        "http://www.americanapparel.com/en/california-fleece-slim-fit-jogger_rsa54240w?c=Black",\
        "http://s7d9.scene7.com/is/image/AmericanApparel/rsa54240w_black?defaultImage=/notavail",\
        'http://www.americanapparel.com/en/the-easy-jean_rsams3334w?c=Dark%20Wash',\
        'http://s7d9.scene7.com/is/image/AmericanApparel/rsams3334w_darkwash_04',\
        'http://www.americanapparel.com/en/peppered-fleece-pullover-hoodie_mt498w?c=Peppered%20Cranberry',\
        'http://s7d9.scene7.com/is/image/AmericanApparel/mt498w_pepperedcranberry?defaultImage=/notavail',\
         request, response)

class BananaPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'B A N A N A - R E P U B L I C',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/banana.png',\
        'Banana Republic',\
        "https://bananarepublic.gap.com/browse/product.do?cid=1105432&pcid=48422&vid=1&pid=363282002",\
        "https://bananarepublic.gap.com/webcontent/0015/519/127/cn15519127.jpg",\
        'https://bananarepublic.gap.com/browse/product.do?cid=1107722&pcid=1107721&vid=1&pid=361080002',\
        'https://bananarepublic.gap.com/webcontent/0015/628/446/cn15628446.jpg',\
        'https://bananarepublic.gap.com/browse/product.do?cid=1093558&pcid=29818&vid=1&pid=266976012',\
        'https://bananarepublic.gap.com/webcontent/0014/573/883/cn14573883.jpg',\
         request, response)

class BloomPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'B L O O M I N G D A L E S',\
        "Although a bit on the pricier side, Bloomingdales expectations of quality apparel exceeds that of its many major competitors. Bloomingdales robust collection of jewelry, accessories, clothing, and handbags makes it a top retailer on many fashion enthusiasts radars. If your fashion standards only demand to be beaten, then Bloomingdales is your one-stop style shop.",\
        'This is where our opinion will go',\
        'images/bloom.png',\
        'Bloomingdales',\
        "https://www.bloomingdales.com/shop/product/michael-michael-kors-kelsey-large-nylon-backpack?ID=2854882&CategoryID=1000369#fn=ppp%3Dundefined%26sp%3D1%26rId%3D132%26spc%3D228%26spp%3D7%26pn%3D1%7C3%7C7%7C228%26rsid%3Dundefined%26smp%3DmatchNone",\
        "https://images.bloomingdalesassets.com/is/image/BLM/products/0/optimized/9761510_fpx.tif?wid=1200&qlt=90,0&layer=comp&op_sharpen=0&resMode=sharp2&op_usm=0.7,1.0,0.5,0&fmt=jpeg",\
        'https://www.bloomingdales.com/shop/product/aqua-freedom-whisper-hoop-earrings-100-exclusive?ID=1778332&CategoryID=3628#fn=ppp%3Dundefined%26sp%3D1%26rId%3D132%26spc%3D1641%26spp%3D2%26pn%3D1%7C19%7C2%7C1641%26rsid%3Dundefined%26smp%3DmatchNone',\
        'https://images.bloomingdalesassets.com/is/image/BLM/products/4/optimized/9199134_fpx.tif?wid=1200&qlt=90,0&layer=comp&op_sharpen=0&resMode=sharp2&op_usm=0.7,1.0,0.5,0&fmt=jpeg',\
        'https://www.bloomingdales.com/shop/product/ag-jacket-robyn-denim?ID=919022&CategoryID=1001521#fn=ppp%3Dundefined%26sp%3D1%26rId%3D132%26spc%3D1203%26spp%3D18%26pn%3D1%7C14%7C18%7C1203%26rsid%3Dundefined%26smp%3DmatchNone',\
        'https://images.bloomingdalesassets.com/is/image/BLM/products/5/optimized/8452505_fpx.tif?wid=1200&qlt=90,0&layer=comp&op_sharpen=0&resMode=sharp2&op_usm=0.7,1.0,0.5,0&fmt=jpeg',\
         request, response)

class ExpressPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'E X P R E S S',\
        'Under CEO David Komberg, Express has expanded to encompass 641 factions as of January 2015. The catalog of clothing here mostly pertains to young women and men.',\
        'This is where our opinion will go',\
        'images/express.png',\
        'Express',\
        "https://www.express.com/clothing/men/double-knit-exp-hem-hoodie/pro/05327570/color/BLACK",\
        "https://images.express.com/is/image/expressfashion/0022_05327570_0058_f028?cache=on&wid=960&fmt=jpeg&qlt=85,1&resmode=sharp2&op_usm=1,1,5,0&defaultImage=Photo-Coming-Soon",\
        'https://www.express.com/clothing/men/extra-slim-blue-cotton-sateen-stretch-suit-jacket/pro/04371540/color/BLUE',\
        'https://images.express.com/is/image/expressfashion/0039_04371540_1837_a115?cache=on&wid=960&fmt=jpeg&qlt=85,1&resmode=sharp2&op_usm=1,1,5,0&defaultImage=Photo-Coming-Soon',\
        'https://www.express.com/clothing/men/classic-fit-10-inch-belted-flat-front-shorts/pro/03532981/color/WHITE',\
        'https://images.express.com/is/image/expressfashion/0026_03532981_0001_e1_f019?cache=on&wid=960&fmt=jpeg&qlt=85,1&resmode=sharp2&op_usm=1,1,5,0&defaultImage=Photo-Coming-Soon',\
         request, response)

class F21Page(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'F O R E V E R - 2 1',\
        'Forever 21 bravely embraces the quirkier and funkier nature of fashion while carefully treading the line between whats too weird and whats not. Those looking for a unique treat each visit to either their site or store will be pleasantly surprised to the plethora of tasteful accessories and apparel more so catered to young ladies.',\
        'This is where our opinion will go',\
        'images/f21.png',\
        'Forever 21',\
        "https://www.forever21.com/us/shop/catalog/Product/21MEN/mens-jackets-and-coats-trenches/2000205979?variantid=&recid=product6_rr-_-35;-_-2000205979-_-4408-_-5",\
        "https://www.forever21.com/images/1_front_750/00205979-01.jpg",\
        'https://www.forever21.com/us/shop/catalog/product/f21/top_blouses/2000272481',\
        'https://www.forever21.com/images/1_front_750/00272481-03.jpg',\
        'https://www.forever21.com/us/shop/catalog/product/f21/acc_hat/2000274206',\
        'https://www.forever21.com/images/1_front_750/00274206-01.jpg',\
         request, response)

class GapPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'G A P',\
        'Its headquarters located in San Fransisco, California, Gap is home to a wide variety of clothing. This all became possible through its co-founders Donald and Doris Fisher. Gap is home to many subsidiaries including Old Navy, Banana Republic and more.',\
        'This is where our opinion will go',\
        'images/gap.png',\
        'Gap',\
        "https://www.gap.com/browse/product.do?cid=1113995&pcid=17076&vid=1&pid=318933002",\
        "https://www.gap.com/webcontent/0015/440/691/cn15440691.jpg",\
        'https://www.gap.com/browse/product.do?cid=1113686&pcid=5156&vid=1&pid=228597082',\
        'https://www.gap.com/webcontent/0015/354/028/cn15354028.jpg',\
        'https://www.gap.com/browse/product.do?cid=1008446&pcid=13658&vid=1&pid=336991132',\
        'https://www.gap.com/webcontent/0015/493/250/cn15493250.jpg',\
         request, response)

class HMPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'H & M',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/hm-logo.png',\
        'H&M',\
        "http://www2.hm.com/en_us/productpage.0631735001.html",\
        "http://lp2.hm.com/hmgoepprod?set=source[/8a/5c/8a5c6a561d73203b2b0b8c6faf5018583a34ccb9.jpg],origin[dam],category[],type[DESCRIPTIVESTILLLIFE],hmver[1]&call=url[file:/product/style]",\
        "http://www2.hm.com/en_us/productpage.0441386004.html",\
        "http://lp2.hm.com/hmgoepprod?set=source[/2b/3f/2b3f3e5934822ca955e4db065d8edf3e8961e167.jpg],origin[dam],category[men_trousers_joggers],type[LOOKBOOK],res[m],hmver[1]&call=url[file:/product/fullscreen]",\
        "http://www2.hm.com/en_us/productpage.0619580006.html",\
        "http://lp2.hm.com/hmgoepprod?set=source[/4c/90/4c905aa7a0940191666f01bfa64b9458e41f298d.jpg],origin[dam],category[ladies_shorts],type[LOOKBOOK],res[m],hmver[1]&call=url[file:/product/fullscreen]",\
        request, response)

class HollPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'H O L L I S T E R',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/hollister.png',\
        'Hollister',\
        "https://www.hollisterco.com/shop/us/p/-11904789?categoryId=12600&seq=03&faceout=model",\
        "https://anf.scene7.com/is/image/anf/hol_215416_03_model1?$product-ofp-hol-v1$",\
        'https://www.hollisterco.com/shop/us/p/-11905427?categoryId=12556&seq=04',\
        'https://anf.scene7.com/is/image/anf/hol_218468_04_prod1?$product-hol-v1$&wid=800&hei=1000',\
        'https://www.hollisterco.com/shop/us/p/-11904528?categoryId=16402&seq=03',\
        'https://anf.scene7.com/is/image/anf/hol_211227_03_prod1?$product-hol-v1$&wid=800&hei=1000',\
         request, response)

class LuluPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'L U L U L E M O N',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/lulu.png',\
        'LuluLemon',\
        "https://shop.lululemon.com/p/women-pants/Dance-Studio-Pant-III-R-MD/_/prod8250314?color=0151",\
        "https://images.lululemon.com/is/image/lululemon/LW5AESR_0151_1?$image_carousel-lg$",\
        'https://shop.lululemon.com/p/women-scarves-gloves/Long-Weekend-Wrap/_/prod8980181?color=0002',\
        'https://images.lululemon.com/is/image/lululemon/LW9BA2S_0002_1?$image_carousel-lg$',\
        'https://shop.lululemon.com/p/men-ss-tops/Metal-Vent-Tech-SS-Henley/_/prod6750185?color=0572',\
        'https://images.lululemon.com/is/image/lululemon/LM3AT9S_0572_1?$image_carousel-lg$',\
         request, response)

class OldPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'O L D - N A V Y',\
        'Old Navy was originally named Gap Warehouse, but was later renamed to become a separate entity. It was then established in March of 1994, when it was named after a bar in Paris.',\
        'This is where our opinion will go',\
        'images/old.png',\
        'Old Navy',\
        "https://oldnavy.gap.com/browse/product.do?cid=89219&pcid=20408&vid=1&pid=202834062",\
        "https://oldnavy.gap.com/webcontent/0014/955/819/cn14955819.jpg",\
        'https://oldnavy.gap.com/browse/product.do?cid=1084902&pcid=10018&vid=1&pid=221779002',\
        'https://oldnavy.gap.com/webcontent/0015/436/113/cn15436113.jpg',\
        'https://www.gap.com/browse/product.do?cid=1113685&pcid=5225&vid=1&pid=306528032',\
        'https://www.gap.com/webcontent/0015/517/758/cn15517758.jpg',\
         request, response)

class UnPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'U N I Q L O',\
        'Uniqlo embraces the simplicity, longevity, and quality of Japanese values - and that is evident in their wide selection of affordable apparel. Enthusiasts familiar with popular clothing lines such as H&M or Forever 21 will feel right at home with Uniqlos unique approach to subtlety.',\
        'This is where our opinion will go',\
        'images/uni.png',\
        'Uniqlo',\
        "https://www.uniqlo.com/us/en/men-denim-jogger-pants-405640.html?dwvar_405640_color=COL68&cgid=men-multibuy-pants-and-jeans#start=31&cgid=men-multibuy-pants-and-jeans",\
        "https://uniqlo.scene7.com/is/image/UNIQLO/goods_68_405640?$pdp-medium$",\
        'https://www.uniqlo.com/us/en/women-ultra-stretch-jeans-409032.html?dwvar_409032_length=032&cgid=women-jeans#ultrastretch=&start=5&cgid=women-jeans',\
        'https://uniqlo.scene7.com/is/image/UNIQLO/goods_00_409032?$prod$',\
        'https://www.uniqlo.com/us/en/women-mercerized-cotton-french-sleeve-short-sleeve-t-shirt-410051.html?dwvar_410051_color=COL68&cgid=women-t-shirts-and-tops#start=5&cgid=women-t-shirts-and-tops',\
        'https://uniqlo.scene7.com/is/image/UNIQLO/goods_68_410051?$prod$',\
         request, response)

class UrbPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'U R B A N O U T F I T T E R S',\
        'Owned by Richard Hayne, urban outfitters headquarters is located in Philly, Pennsylvania. There are a total of 402 retail stores, and mostly selling what is known as "hipster clothing".',\
        'This is where our opinion will go',\
        'images/urb.png',\
        'Urban OutFitters',\
        "https://www.urbanoutfitters.com/shop/bdg-core-denim-trucker-jacket-001?category=mens-jackets&color=092",\
        "https://images.urbanoutfitters.com/is/image/UrbanOutfitters/39763123_092_b?$xlarge$&hei=900&qlt=80&fit=constrain",\
        'https://www.urbanoutfitters.com/shop/uo-colette-stretch-linen-mini-dress?category=dresses&color=049',\
        'https://images.urbanoutfitters.com/is/image/UrbanOutfitters/45821824_049_b?$xlarge$&hei=900&qlt=80&fit=constrain',\
        'https://www.urbanoutfitters.com/shop/bdg-corduroy-utility-mini-skirt?category=womens-utility&color=025',\
        'https://images.urbanoutfitters.com/is/image/UrbanOutfitters/47254149_025_b?$xlarge$&hei=900&qlt=80&fit=constrain',\
         request, response)

class ZaraPage(MerchantPage):
    def __init__(self,request,response):
        MerchantPage.__init__(self,\
        'Z A R A',\
        'American Apparel was founded in 1989 by Dov Charney, and has grown ever since. Their last reported revenue graft showed the retailer grossed 604 million dollars in a year. However, their fall was soon met and now there are no retailer stores.',\
        'This is where our opinion will go',\
        'images/zara.png',\
        'Zara',\
        "https://www.zara.com/us/en/mixed-ribbed-blouse-p07563246.html?v1=6778122&v2=1074623",\
        "https://static.zara.net/photos///2018/I/0/1/p/7563/246/800/2/w/1024/7563246800_1_1_1.jpg?ts=1532071894414",\
        'https://www.zara.com/us/en/sweatshirt-with-pouch-pocket-p01701317.html?v1=7311520&v2=1079150',\
        'https://static.zara.net/photos///2018/I/0/2/p/1701/317/401/6/w/1024/1701317401_1_1_1.jpg?ts=1531981903167',\
        'https://www.zara.com/us/en/athletic-beige-leather-shoes-p12519302.html?v1=6453363&v2=1079370',\
        'https://static.zara.net/photos///2018/I/1/2/p/2519/302/102/2/w/1024/2519302102_1_1_1.jpg?ts=1532016731283',\
         request, response)

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
        title_dict['logout'] = 'Log out'

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
