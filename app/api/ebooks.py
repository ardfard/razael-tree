from flask import Blueprint, request

from ..services import ebooks, category

bp = Blueprint('ebooks', __name__, url_prefix='/ebooks')

@bp.route('/')
def list():
    """Returns a list of ebook instances."""
    return ebooks.all()

 @bp.route('/<ebook_id>')
 def show(ebook_id):
 	"""return a product instance"""
 	return ebooks.get_or_404(ebook_id)

@bp.route('/<category>')
def show_category(category):
	"""return all product in given category"""
	return category.find(name=category)[0]

