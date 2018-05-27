from app import db
from flask import flash, request, redirect, url_for
from app.models import User

def register_user():
  form = request.form
  user = User(
    name=form.get('name'),
    email=form.get('email'),
    password=form.get('password'),
    is_admin=False
  )
  db.session.add(user)
  db.session.commit()
  flash("Succes register users.")
  return redirect(url_for('login'))
