from google.appengine.ext import ndb

class User(ndb.Model):
    user_name = ndb.StringProperty(required=True)
    real_name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty()

class Comment(ndb.Model):
    #user = ndb.StringProperty
    content = ndb.StringProperty(required=True)
    brand = ndb.StringProperty(required=True)
