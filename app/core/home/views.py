from app import app
from flask import render_template, request
from flask_login import login_required
from .home import search_home

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
  if request.method == 'POST':
    return search_home()
  return render_template('home.html')

@app.route('/transactions', methods=['GET', 'POST'])
@login_required
def transactions():
  if request.method == 'POST':
    return search_home()
  return render_template('home.html')

@app.route('/categories')
@login_required
def categories():
  return render_template('categories/index.html')