#from hashlib import md5
from app import db
from app import app
import flask.ext.whooshalchemy as whooshalchemy


ebooks_authors = db.Table('authors',
                   db.Column('ebook_id',db.Integer, db.ForeignKey('ebook.id')),
                   db.Column('author_id', db.Integer, db.ForeignKey('author.id')),
                   )

ebooks_categories = db.Table('categories',
                      db.Column('ebook_id', db.Integer, db.ForeignKey('ebook.id'))
                      db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
                      )


class Ebook(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(128))
    date = db.Column(db.DateTime)
    format = db.Column(db.Integer)
    authors = db.relationship('Author', secondary=ebooks_authors,
                              backref='books', lazy='dynamic')
    Categories = db.relationship('Category', secondary=ebooks_categories,
                                 backref='books', lazy='dynamic')


class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))


#class User(db.Model):
#    id = db.Column(db.Integer, primary_key = True)
#    nickname = db.Column(db.String(64), unique = True)
#    email = db.Column(db.String(120), index = True, unique = True)
#    role = db.Column(db.SmallInteger, default = ROLE_USER)
#    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
#    about_me = db.Column(db.String(140))
#    last_seen = db.Column(db.DateTime)
#    followed = db.relationship('User', 
#        secondary = followers, 
#        primaryjoin = (followers.c.follower_id == id), 
#        secondaryjoin = (followers.c.followed_id == id), 
#        backref = db.backref('followers', lazy = 'dynamic'), 
#        lazy = 'dynamic')
 #    @staticmethod
#    def make_unique_nickname(nickname):
#        if User.query.filter_by(nickname = nickname).first() == None:
#            return nickname
#        version = 2
#        while True:
#            new_nickname = nickname + str(version)
#            if User.query.filter_by(nickname = new_nickname).first() == None:
#                break
#            version += 1
#        return new_nickname
#        
#    def is_authenticated(self):
#        return True

#    def is_active(self):
#        return True

#    def is_anonymous(self):
#        return False

#    def get_id(self):
#        return unicode(self.id)
#    def __repr__(self):
#        return '<User %r>' % (self.nickname)    
#        
       
#whooshalchemy.whoosh_index(app, Post)
