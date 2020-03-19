from apps.app import app
from apps import view
from apps.config import HOST,PORT


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
