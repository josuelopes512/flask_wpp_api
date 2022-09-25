import click
from flask.cli import FlaskGroup
from threading import Thread
import os
from time import sleep

from . import create_app_wsgi


@click.group(cls=FlaskGroup, create_app=create_app_wsgi)
def main():
    """Management script for the flask_wpp_api application."""
    Thread(target=os.system, args=("startwpp.bat",)).start()
    sleep(1)


if __name__ == "__main__":  # pragma: no cover
    main()
