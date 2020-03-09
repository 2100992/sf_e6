import bottle

@bottle.route("/bottle/")
def index():
    return "hello, Docker! (from bottle)"

bottle.run(host="0.0.0.0", port=5000)