
from flask import Flask, abort, render_template
from briochefood.ext import configuration

def minimal_app():
  app = Flask(__name__)
  configuration.init_app(app)
  return app

def create_app():
  app = minimal_app()
  configuration.load_extensions(app)
  return app

