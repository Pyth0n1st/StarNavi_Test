from flask import Blueprint

bp = Blueprint('main', __name__)

from app.ui.main import routes
