import os
from conf.default import *

module_path = os.environ.get('DJANGO_CONF', 'conf.local')
module = __import__(module_path, globals(), locals(), ['*'])
for k in dir(module):
    if not k.startswith("__"):
        locals()[k] = getattr(module, k)