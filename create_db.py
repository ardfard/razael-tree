import os
from app.ebooks.constants import EBOOK_FORMAT
from app.ebooks.models import Ebook, Category, Author
from app import db
import re

EBOOK_REPO_PATH = os.path.join(os.getcwd(),"ebooks_repo")
extensions = tuple(EBOOK_FORMAT.iterkeys())

def is_format_accepted(file):
    if file.endswith(extensions):
        return True
    else :
        return False

def parse_authors(authors_str):
    """ Parse authors from authors in filename format """

    temp = re.sub('[\[\]]','',authors_str).split(';')
    authors_name = [a.replace("_"," ") for a in temp]
    author = map(get_or_create_author, authors_name)
    return author

def get_or_create_category(category_name):
    category = Category.query.filter_by(name = category_name).first()
    if category:
        return category
    else :
        return Category(category_name)

def get_or_create_author(author_name):
    author = Author.query.filter_by(name = author_name).first()
    if author:
        return author
    else:
        return Author(author_name)

def create_and_add_ebook_from_filename(file, root, db):
    """ Create an Ebook instance from filename """


    relpath = os.path.relpath(root,EBOOK_REPO_PATH)
    categories = os.path.split(relpath)
    categories = map(get_or_create_category, categories)
    filename,ext= os.path.splitext(file)
    title,edition,authors,year = filename.split(',')
    authors = parse_authors(authors)
    file_path = root + file
    ebook = Ebook(title, EBOOK_FORMAT[ext],file_path, year, edition, authors, categories)
    db.session.add(ebook)
    db.session.commit()

if __name__ == '__main__':
    db.create_all()
    for root, directories, files in os.walk(EBOOK_REPO_PATH):
        for file in files :
            if is_format_accepted(file):
                create_and_add_ebook_from_filename(file, root, db)

    for ebook in Ebook.query.all():
        print ebook.title, [category.name for category in ebook.categories]

    for c in Category.query.all():
        print c.name
