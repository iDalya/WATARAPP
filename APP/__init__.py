from flask import Flask

app = Flask(__name__)

from app.views import admin_views
from app.views import user_views
from app.views import public_views
