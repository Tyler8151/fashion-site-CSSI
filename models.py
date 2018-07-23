from google.appengine.ext import ndb

class User(ndb.Model):
    user_name = ndb.StringProperty(required=True)
    comment = ndb.FloatProperty(required=True)


class Store(ndb.Model):
    title = ndb.StringProperty()
    url = ndb.StringProperty()
