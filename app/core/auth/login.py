from app import db
from flask import flash, request, redirect, url_for, render_template
from flask_login import login_user as login
from app.models import User
from .validators import old, errors

def login_user():
  form = request.form
  user = User.query.filter_by(email=form.get('email')).first()
  if user.verify_password(form.get('password')):
    login(user)
    return redirect(url_for('home'))
  errors['password'] = 'Your password is invalid';
  return render_template('login.html', old=old, errors=errors)
