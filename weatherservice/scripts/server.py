# -*- coding: utf-8 -*-
"""
"""
import os
import socket
import logging
import platform
import logging.config
from optparse import OptionParser

from weatherservice.app import create_app


def logging_setup():
    """Log to the console.

    :returns: A configured root log instance.

    """
    hostname = platform.node()
    addr = socket.gethostbyname(hostname)

    cfg = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                'format': (
                    '%(asctime)s %(funcName)s %(name)s '
                    '%(levelname)s %(message)s'
                )
            },
        },
        'handlers': {
            'default': {
                'level': 'NOTSET',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': 'DEBUG',
                'propagate': True
            },
            'newrelic': {
                'handlers': ['default'],
                'level': 'INFO',
                'propagate': False
            },
            'werkzeug': {
                'handlers': ['default'],
                'level': 'WARN',
                'propagate': False
            },
        }
    }

    logging.config.dictConfig(cfg)

    return logging.getLogger()


def main():
    """The scp_report_server main.

    """

    parser = OptionParser()

    parser.add_option(
        "-i", "--interface", action="store", dest="interface",
        default='0.0.0.0',
        help="The interface to bind to (default: %default)."
    )
    parser.add_option(
        "-p", "--port", action="store", dest="port",
        default=7080,
        help="The TCP port to listen on (default: %default)."
    )

    (options, args) = parser.parse_args()

    log = logging_setup()

    try:
        log.info(u"Creating applicantion.")

        app = create_app()

        log.info(u"Applicantion created OK")

        log.info(u"starting the server on {}:{}...".format(
            options.interface,
            options.port
        ))
        port = int(options.port)
        log.info(u"Server Running on: http://{}:{}".format(
            options.interface, port
        ))
        app.run(
            host=options.interface,
            port=port,
            use_reloader=False,
        )

    except KeyboardInterrupt:
        log.info(u"Ctrl-C caught, exit time.")


if __name__ == '__main__':
    main()
