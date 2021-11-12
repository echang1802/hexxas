
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from hexxas.auth import login_required
from hexxas.db import get_db

bp = Blueprint('menu', __name__)

@bp.route('/')
def index():
    return render_template('menu/index.html')
