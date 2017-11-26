#! /usr/bin/env pytho
# -*- coding: utf-8 -*-

"""
Usage:
    simple-sanic [options]
    simple-sanic -h | --help

Options:
    -p --port PORT      Specify alternate port [default: 8000]
    -b --bind ADDRESS   Specify alternate bind address [default: 0.0.0.0]
    -h, --help          Show this help message and exit.
"""

import os.path

from sanic import Sanic
import docopt


def main():
    args = docopt.docopt(__doc__)

    port = int(args['--port'])
    host = args['--bind']

    app = Sanic(__name__, log_config=None)

    if os.path.exists('index.html'):
        app.static('/', './index.html')

    app.static('/', '.')
    app.run(host=host, port=port)


if __name__ == '__main__':
    main()
