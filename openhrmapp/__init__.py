from flask import Flask
from openhrmapp.core.views import core
from openhrmapp.error_pages.handlers import error_pages

app = Flask(__name__)

app.register_blueprint(core)
app.register_blueprint(error_pages)
