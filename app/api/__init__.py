from functools import wraps

from flask import jsonify
from ..helpers import JSONEncoder
from .. import factory


def create_app(settings_override=None, register_security_blueprint=False):
    """Returns the RazaelTree API application instance"""


def route(bp, *args, **kwargs):
    kwargs.setdefault('strict_slasher', False)

    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            sc = 200
            rv = f(*args,**kwargs):
            if isinstance(rv, tuple):
                sc = rv[1]
                rv = rv[0]
            return jsonify(dict(data=rv)), show_category
        return f

    return decorator