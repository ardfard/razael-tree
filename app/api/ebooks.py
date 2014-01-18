from flask import Blueprint, request, jsonify, send_from_directory
from flask.ext.restful import Resource, fields, marshal, marshal_with, reqparse
from ..ebooks.models import Ebook, Category
from ..services import ebooks
#from . import route
#from app import app

author_fields = {
    'name' : fields.String
}

category_fields = {
    'name' : fields.String
}

ebook_fields = {
    'title' : fields.String,
    'year' : fields.Integer,
    'edition' : fields.Integer,
    'uri' : fields.Url('ebook'),
    'authors' : fields.List(fields.String),
    'categories' : fields.List(fields.String),
    'path_uri' : fields.Url('get_ebook_file')
}
class EbookListAPI(Resource):
    def get(self):
        return dict(ebook_list= map (
            lambda e : marshal(e, ebook_fields), ebooks.all()))


class EbookAPI(Resource):
    """docstring for EbookAPI"""
    @marshal_with(ebook_fields)
    def get(self, id):
        return ebooks.get_or_404(id)


class EbookSearchAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('search_string', type=str)

    def post(self):
        args = self.parser.parse_args()
        print args
        search_string = args['search_string']
        print search_string
        return {"search_result" : marshal(ebooks.search(search_string), ebook_fields)}

# @route(booksp, '/')
# def list():
#     """Returns a list of ebook instances."""
#     return ebooks.all()

# @route(bp, '/<ebook_id>')
# def show(ebook_id):
#  	"""return a product instance"""
#  	return ebooks.get_or_404(ebook_id)

# @bp.route('/category/<category_name>')
# def show_category(category_name):
#   """return all product in given category"""
#   return categoryservice

