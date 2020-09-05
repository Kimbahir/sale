from flask import Flask
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'df61f5fe12eb40792e85b284ead07d51'


logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s:\t%(message)s')

from app.flask_web import routes_webgui
