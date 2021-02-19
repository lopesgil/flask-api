from flask import Flask

app = Flask(__name__)

from quotr import routes
