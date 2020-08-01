import os
from flask import Flask
from delivery.ext import config


def create_app():
    """Factory principal"""
    app = Flask(__name__)
    config.init_app(app)

    return app

