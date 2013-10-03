from app import db
from app import app


ebooks_authors = db.Table('authors',
                   db.Column('ebook_id',db.Integer, db.ForeignKey('ebook.id')),
                   db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
                   )

ebooks_categories = db.Table('categories',
                      db.Column('ebook_id', db.Integer, db.ForeignKey('ebook.id')),
                      db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
                      )


class Ebook(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(128))
    year = db.Column(db.Integer)
    edition = db.Column(db.SmallInteger)
    format = db.Column(db.SmallInteger)
    path = db.Column(db.String(128))
    authors = db.relationship('Author', secondary=ebooks_authors,
                              backref='books', lazy='dynamic')
    categories = db.relationship('Category', secondary=ebooks_categories,
                                 backref='books', lazy='dynamic')

    def __init__(self, title, format, path, year=None,edition=None, authors =[], categories = []):
        self.title = title
        self.format = format
        self.year = year
        self.path = path
        self.edition = edition
        self.authors = authors
        self.categories = categories

    def __unicode__(self):
        return "ebook {} {} {}".format(self.title, self.year, '['+" ".join(self.authors)+']')

    def serialize(self):
        return {'title' : self.title,
                'format': self.format,
                'year'  : self.year,
                'edition': self.edition,
                'authors': [author.name for author in self.authors],
                'categories':[category.name for category in self.categories]
                }


class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128), unique=True)

    def __init__(self, name):
        self.name = name

    def __unicode__(self):
        return self.name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128), unique=True)

    def __init__(self, category_name):
        self.name = category_name

    def __unicode__(self):
        return self.name
