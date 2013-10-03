from flask import Blueprint, request, jsonify

from ..ebooks.models import Ebook, Category

bp = Blueprint('ebooks', __name__, url_prefix='/ebooks')

@bp.route('/')
def list():
    """Returns a list of ebook instances."""
    return jsonify(ebook_list=[e.serialize() for e in Ebook.query.all()])

@bp.route('/id/<ebook_id>')
def show(ebook_id):
 	"""return a product instance"""
 	return jsonify(Ebook.query.get(ebook_id).serialize())

@bp.route('/category/<category_name>')
def show_category(category_name):
	"""return all product in given category"""
	return Category.query.filter_by(name=category_name).first()

