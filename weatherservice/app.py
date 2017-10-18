# -*- coding: utf-8 -*-
"""The app module, containing the app factory function.

"""
import json
import logging
import tempfile

from flask import Flask
from flask import Response

from weatherservice import views
from weatherservice.config import Configuration


def get_log(e=None):
    return logging.getLogger("{0}.{1}".format(__name__, e) if e else __name__)


def create_app(config={}):
    """An application factory, as explained here:

    http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.

    """
    app = Flask(__name__, static_url_path=tempfile.tempdir)

    app.config.from_object(Configuration)

    app.url_map.strict_slashes = False

    register_blueprints(app)
    register_errorhandlers(app)

    return app


def register_errorhandlers(app):
    """Convert all errors in an inspectable JSON.

    """
    log = get_log('register_errorhandlers')

    def render_error(error):
        error_code = getattr(error, 'code', 500)

        log.debug("error_code: {} using JSON reponse.".format(error_code))
        if error_code == 500:
            message = error.message
        else:
            message = error.description

        log.error(u'Error {}: {}'.format(error_code, message), exc_info=error)
        message = json.dumps(dict(error_code=error_code, message=message))

        resp = Response(message, mimetype='application/json')
        returned = (resp, error_code)

        return returned

    # no 402 in the flask internal dict so this causes KeyErrors:
    for errcode in [400, 401, 403, 404, 405, 406, 409, 500]:
        app.register_error_handler(errcode, render_error)


def register_blueprints(app):
    """Register Flask blueprints.

    """
    app.register_blueprint(views.blueprint)
