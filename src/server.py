from flask import Flask


import config
from model.abc import db

server = Flask(__name__)
server.debug = config.DEBUG


from route.common import common_blueprint
server.register_blueprint(common_blueprint)

from route.user import user_blueprint
server.register_blueprint(user_blueprint)


server.run(host=config.HOST, port=config.PORT)
