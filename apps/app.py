from flask import Flask

from flask_caching import Cache

from apps.config import config


app = Flask(__name__)

app.config.from_mapping(config)

cache = Cache(app)
