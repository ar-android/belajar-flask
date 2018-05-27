# Views

from flask import render_template
from flask_login import login_required
from app import app
from . import core

@app.route('/')
def index():
  return render_template('index.html')
