===============
weather_service
===============

.. contents::


Introduction
------------

This is a Python/Flask service which provides an API to get a forecast for a
given city.

The service requires an API key from https://www.openweathermap.org
(free registration required). This API's backend uses the Open Weather API
endpoint https://openweathermap.org/forecast5.


Getting it running
------------------

The implementation of this service has some problems that need to be fixed
before it will run. Once the project has been set up you should be able to run
the service by calling:

.. code-block:: bash

	$ weather_service
	2017-10-05 13:52:39,047 main root INFO Creating applicantion.
	2017-10-05 13:52:39,050 main root INFO Applicantion created OK
	2017-10-05 13:52:39,051 main root INFO starting the server on 0.0.0.0:7080...
	2017-10-05 13:52:39,051 main root INFO Server Running on: http://0.0.0.0:7080


Existing API
------------

I would like to make the following calls against this web service using "curl".
The submitted result will be put through automated testing to verify the API
is working.

When the service is running it can be checked using the ping endpoint:

.. code-block:: bash

	$ curl http://localhost:7080/ping
	{
	  "name": "weatherservice",
	  "status": "ok",
	  "version": "1.0.0"
	}

The weather endpoint has the form:

.. code-block:: bash

	curl http://<host:ip>/<city>/<date>/<hour minute>/

	$ curl http://localhost:7080/london/20171005/2200/
	{
	  "description": "broken clouds",
	  "humidity": "66%",
	  "pressure": 1027.51,
	  "temperature": "285.25C"
	}

The service also supports recovering just the fields: description, humidity,
pressure & temperature:

.. code-block:: bash

	curl http://<host:ip>/<city>/<date>/<hour minute>/<field>

	$ curl http://localhost:7080/london/20171005/2200/humidity
	{
	  "humidity": "66%"
	}

	$ curl http://localhost:7080/london/20171005/2200/temperature
	{
	  "temperature": "285.25C"
	}


When no data is found for the date and time given the API will respond with:

.. code-block:: bash

	$ curl http://localhost:7080/london/21171005/2200/temperature
	{
	  "message": "No data for 2117-10-05 22:00",
	  "status": "error"
	}


New Features Required
---------------------

 - I want the temperature in Fahrenheit, Kelvin or Celcius, how could I
   specify this in API calls? Implement.
 - Please restrict API access so it can be revoked at a later stage. If the
   environment variable NO_AUTH_FOR_TEST=1 is set it should disable
   authorisation to aid automated verification of the existing API.
 - Return some appropriate data when requesting a time between two times that
   the https://openweathermap.org/forecast5 data set supports.


Bonus Features (Optional)
-------------------------

 - A docker container which can be configured with the API key.
 - A running service hosted by a cloud provider.
