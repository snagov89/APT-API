""" Modules """

import os
import logging
from logging.handlers import TimedRotatingFileHandler
from colorama import Fore, Style, init
from flask import Flask, render_template

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    key_func=get_remote_address,
    storage_uri=os.getenv("mongo_connection_string"),
)

def create_app():

    app = Flask(__name__)

    limiter.init_app(app)

    return app
