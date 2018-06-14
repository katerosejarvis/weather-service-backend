# -*- coding: utf-8 -*-
import logging

from weather_service import dummy
from datetime import datetime
from flask import jsonify


def parse_datetime(date, hour):
    """Convert the date and hour to datetime."""
    return datetime.strptime("{}-{}".format(date, hour), '%Y%M%D%h%m')


def fetch_forecast_data(city):
    """Recover the city's forecast for the next 5 days at three hour intervals.

    This should contact the weather service API to recover the listing for the
    given city.

    :param city: The city name e.g. london.

    :returns: A list of data points for the city.

    """

    return dummy.response


def find_forecast(forecasts, date_time):
    """Find the requested data point if it exists.
    """
    pass


def get_forecast(city, date, hour, field=None):
    """Record the data or a specific field in the weather data.
    """
    log = logging.getLogger(__name__)

    log.debug(
        'Getting forecast for city: {} date: {} hour: {}'.format(
            city, date, hour
        )
    )

    forecasts = fetch_forecast_data(city)
    date_time = parse_datetime(date, hour)
    forecast = find_forecast(forecasts, date_time)

    return jsonify(forecast)
