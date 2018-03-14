import json
from functools import wraps

def to_json(func):
    @wraps(func)
    def inner(*args,**kwargs):
        value = func(*args,**kwargs)
        return json.dumps(value)
    return inner