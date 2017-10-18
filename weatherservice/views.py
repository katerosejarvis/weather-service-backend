# -*- coding: utf-8 -*-
"""
"""
import logging

from flask import Blueprint
from flask import jsonify

from weatherservice import backend


def get_log(e=None):
    return logging.getLogger("{0}.{1}".format(__name__, e) if e else __name__)


blueprint = Blueprint('public', __name__)


@blueprint.route('/')
@blueprint.route('/ping')
def ping():
    """This is used to 'ping' the web service to check if its running.

    :returns: a status dict which the configured view will return as JSON.

    The dict has the form::

        dict(
            status="ok",
            name="weatherservice",
            version="<version number of service>"
        )

    """
    return jsonify(dict(
        status="ok",
        name="weatherservice",
        version=open('VERSION').read().strip(),
    ))


@blueprint.route('/<city>/<date>/<hour>', methods=['GET'])
def get_complete_forecast(city, date, hour):
    """Recover the complete dataset returned or handle no data found.
    """
    return backend.get_forecast(city, date, hour)
