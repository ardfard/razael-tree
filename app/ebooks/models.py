from app import db
from app import app


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
