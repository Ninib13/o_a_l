from flask import Flask
import time

app = Flask(__name__)

time.sleep(10)

from service import routes