
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from hexxas.auth import login_required
from hexxas.db import get_db

bp = Blueprint('menu', __name__)

@bp.route('/')
def index():
    return render_template('menu/main.html')

@bp.route('/about')
def index():
    return render_template('menu/about.html')

@bp.route('/rankings')
def index():
    db = get_db()
    query = """
    SELECT username, battles, battles_won, ROUND(100 * battles_won / battles) as win_ratio
    FROM users
    ORDER BY battles_won DESC
    """
    players = db.execute(query).fetchall()
    return render_template('menu/rankings.html', players = players)
