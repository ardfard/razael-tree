import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'who is the patriot?'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

#MAIL_SERVER = 'gmail.com'
#MAIL_PORT = 25
#MAIL_USE_TLS = False

ADMINS = frozenset(['ardfarde@gmail.com'])

EBOOKS_PER_PAGE = 8
