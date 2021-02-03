
from flask import Flask, jsonify, request, Response
from flask_accept import accept, accept_fallback
import logging
import sys

app = Flask(__name__)

logger = logging.getLogger('werkzeug')
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

mydebug = False
# mydebug = True

@app.route('/', methods=['GET', 'POST'])
@accept_fallback
def hello_world():
    if mydebug: logger.debug("%s - %s - %s" % (request.remote_addr, request.url, request.method))

    return '<p>Hello, World</p>'

@hello_world.support('application/json')
def hello_world_json():
    if mydebug: logger.debug("%s - %s - %s" % (request.remote_addr, request.url, request.method))

    return jsonify(message="Hello, World")

if __name__ == '__main__':
    #
    # app.run(debug=True,host='0.0.0.0')
    #
    # app.run(host='0.0.0.0')
    #
    app.run()
