from ..core import Service
from .models import Ebook,Category


class CategoryService(object):
	__model__ = Category
 		 

class EbooksService(object):
	"""docstring for EbooksService"""
	def __init__(self, arg):
		super(EbooksService, self).__init__()
		self.arg = arg
		