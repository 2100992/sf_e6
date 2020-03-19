import os
from distutils.util import strtobool

HOST = str(os.environ.get('HOST', '127.0.0.1'))
PORT = int(os.environ.get('PORT', '5000'))
# DEBUG = strtobool(os.environ.get('DEBUG', 'True'))


config = {
    "DEBUG": strtobool(os.environ.get('DEBUG', 'True')),            # some Flask specific configs
    # "CACHE_TYPE": "simple",                                       # Flask-Caching related configs
    "CACHE_TYPE": "memcached",                                      # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300,

    'CACHE_MEMCACHED_SERVERS': 'localhost',
    'CACHE_MEMCACHED_USERNAME': 'user',
    'CACHE_MEMCACHED_PASSWORD': 'password',

}
