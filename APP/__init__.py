from flask import Flask

app = Flask(__name__)

from APP.views import admin_views
from APP.views import user_views
from APP.views import public_views