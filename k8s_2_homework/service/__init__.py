from flask import Flask
import time

app = Flask(__name__)

time.sleep(4)

from service import routes