from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.ui.auth import routes
