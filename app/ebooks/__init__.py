from ..core import Service
from .models import Ebook,Category, Author


class CategoryService(Service):
	__model__ = Category


class AuthorService(Service):
	__model__ = Author

class EbooksService(Service):
	"""docstring for EbooksService"""
	__model__ = Ebook

	def __init__(self, *args, **kwargs):
		super(EbooksService,self).__init__(*args, **kwargs)
		self.categories = CategoryService()
		self.authors = AuthorService()

	def _preprocess_params(self, kwargs):
		kwargs = super(EbooksService, self)._preprocess_params(kwargs)
		categories = kwargs.get('categories', [])
		if categories and all(isinstance(c, int) for c in categories):
			kwargs['categories'] = self.categories.get_
		authors = kwargs.get('authors',[])
		if authors and all(isinstance(c, int) for c in authors):
			kwargs['authors'] = self.authors.get_all(*authors)
		return kwargs
