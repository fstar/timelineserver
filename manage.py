# -*- coding: utf-8 -*-

import logging
import os

import click

from app.handler.logger_handler import init_logger

logger = logging.getLogger(__name__)


@click.group()
def cli():
    os.makedirs(os.path.join(os.path.dirname(__file__), 'logs'), exist_ok=True)
    init_logger(os.path.join(os.path.dirname(__file__), 'configs', 'server_log.ini'))
    logger.info('Init app...')


@cli.command()
def run_api_server():
    from app.flask_app import flask_app
    from gunicorn_app import StandaloneApplication
    logger.info('Run api server...')
    options = {'bind': '0.0.0.0:5005'}
    app = StandaloneApplication(flask_app, options)
    app.run()


if __name__ == '__main__':
    cli()
