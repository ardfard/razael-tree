from ..core import Service
from .models import Ebook,Category


class CategoryService(Service):
	__model__ = Category


class EbooksService(Service):
	"""docstring for EbooksService"""
	def __init__(self, *args, **kwargs):
		super(EbooksService,self).__init__(*args, **kwargs)
		self.categories = CategoryService()

	def _preprocess_params(self, kwargs):
		kwargs = super(EbooksService, self)._preprocess_params(kwargs)
		categories = kwargs.get('categories', [])
		if categories and all(isinstance(c, int) for c in categories):
			kwargs['categories'] = self.categories.get_
