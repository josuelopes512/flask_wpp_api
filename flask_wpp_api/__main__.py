import click
from flask.cli import FlaskGroup
from threading import Thread
import os
from time import sleep
import platform

from . import create_app_wsgi


@click.group(cls=FlaskGroup, create_app=create_app_wsgi)
def main():
    """Management script for the flask_wpp_api application."""
    if "Windows" in platform.system():
        Thread(target=os.system, args=("start.bat",)).start()
    else:
        Thread(target=os.system, args=("start.sh",)).start()
    sleep(1)


if __name__ == "__main__":  # pragma: no cover
    main()
