from app.api import ebooks
from app import app

app.register_blueprint(ebooks.bp)
app.run(debug = True)
