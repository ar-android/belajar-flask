# Auth

from flask import render_template, redirect, url_for, flash, request
from flask_login import logout_user, login_required
from app import app, db, csrf
from .validators import errors, old, is_valid_input_register, is_valid_input_login
from .register import register_user
from .login import login_user

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST' and is_valid_input_login():
      return login_user()
  return render_template('auth/login.html', old=old, errors=errors)

@app.route('/register', methods=['GET', 'POST'])
@csrf.exempt
def register():
    if request.method == 'POST' and is_valid_input_register():
      return register_user()
    return render_template('auth/register.html', errors=errors, old=old)

@app.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('login'))

@app.route('/change-password')
@login_required
def change_password():
  return render_template('auth/change-password.html')