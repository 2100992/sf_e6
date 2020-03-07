import bottle

@bottle.route("/")
def index():
    return "hello!"

bottle.run(host="0.0.0.0", port=5000)