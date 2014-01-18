from app import db
from app import app
from app.helpers import JsonSerializer
import flask.ext.whooshalchemy as whooshalchemy


ebooks_authors = db.Table('ebooks_authors',
                   db.Column('ebook_id',db.Integer, db.ForeignKey('ebooks.id')),
                   db.Column('author_id', db.Integer, db.ForeignKey('authors.id'))
                   )

ebooks_categories = db.Table('ebooks_categories',
                      db.Column('ebook_id', db.Integer, db.ForeignKey('ebooks.id')),
                      db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))
                      )


class HiddenEbooksFieldJsonSerializer(JsonSerializer):
    __json_hidden__ = ['books']

def path_to_url(path, ebook):
    return "go to " + path


class EbookJsonSerializer(JsonSerializer):
  __json_hidden__ = ["path"]

  def to_json(self):
      rv = super(EbookJsonSerializer, self).to_json()
      rv['url'] = 'url to ' + self.path
      return rv


class Ebook(EbookJsonSerializer, db.Model):
    __tablename__ = 'ebooks'
    __searchable__ = ['title']

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    year = db.Column(db.Integer)
    edition = db.Column(db.SmallInteger)
    path = db.Column(db.String(255))
    authors = db.relationship('Author', secondary=ebooks_authors,
                              backref=db.backref('books', lazy='joined'))
    categories = db.relationship('Category', secondary=ebooks_categories,
                                 backref=db.backref('books', lazy='joined'))

    def __unicode__(self):
        return "ebook {} {} {}".format(self.title, self.year, '['+" ".join(a.name for a in self.authors)+']')


class Author(HiddenEbooksFieldJsonSerializer, db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128), unique=True)

    def __unicode__(self):
        return self.name


class Category(HiddenEbooksFieldJsonSerializer, db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128), unique=True)

    def __unicode__(self):
        return self.name

whooshalchemy.whoosh_index(app, Ebook)
if __name__ == '__main__':
    ebook = Ebook(title="sugru", year=2010, edition=3, path='path_to_folder',authors=[Author(name='indah'),Author(name='sosro')], categories=[Category(name="indah")])
    print ebook.__unicode__()
