""" Main entry """
# pylint: disable=invalid-name
# pylint: disable=wrong-import-position
import os
from flask import Flask
from flask_script import Manager, Server
from flask_limiter import Limiter
from flask_limiter.util import get_ipaddr


app = Flask(__name__)

config_name = os.environ.get('config')
if config_name:
    app.config.from_object('application.config.'+config_name)
else:
    app.config.from_object('application.config.DevelopmentConfig')
    app.jinja_env.auto_reload = True

limiter = Limiter(app, key_func=get_ipaddr)

manager = Manager(app)
manager.add_command('runserver', Server(
    host="0.0.0.0", port="5009", threaded=True))


from application.api.views import API_BP as api
app.register_blueprint(api, url_prefix="/api")
