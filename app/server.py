import bottle

@bottle.route("/")
def index():
    return "hello!"

bottle.run(host="127.0.0.1", port=5000)