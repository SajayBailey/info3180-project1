from . import db
class UserProfile(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    age = db.Column(db.Integer)
    biography = db.Column(db.String(300))
    created = db.Column(db.DateTime(80))
    profile_pic = db.Column(db.String(256))
    
    id_strt = 50100
    
    def __init__ (self, userid, first_name,last_name,username, age, biography, created, profile_pic):
         self.userid = userid
         self.first_name = first_name
         self.last_name = last_name
         self.username = username
         self.email = email
         self.age = age
         self.biography = biography
         self.created = created
         self.profile_pic = profile_pic
    
    
    
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
