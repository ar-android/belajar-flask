from flask import request
from app.models import User

errors = {}

# Validate input registration users
def is_valid_input_register():
  form = request.form
  is_valid = True
  if not form.get('name'):
    is_valid = False
    add_error_required('name')
  elif not form.get('email'):
    is_valid = False
    add_error_required('email')
  elif not form.get('password'):
    add_error_required('password')
    is_valid = False
  elif not form.get('password') == form.get('password_confirmation'):
    errors['password_confirmation'] = 'Invalid password confirmations.'
    is_valid = False
  elif len(form.get('password')) < 6:
    errors['password'] = 'Password should more than 6 characters.'
    is_valid = False
  return is_valid

# Validate input login users
def is_valid_input_login():
  is_valid = True
  form = request.form
  user = User.query.filter_by(email=form.get('email')).first()
  if not form.get('email'):
    is_valid = False
    add_error_required('email')
  elif not form.get('password'):
    add_error_required('password')
    is_valid = False
  elif user is None:
    errors['email'] = "Email is not registered yet."
  return is_valid

# Get cache input field users
def old(key):
  if request.form.get(key):
    return request.form.get(key)
  return ''

# Add error required field
def add_error_required(field):
    errors[field] = "Field {} is required.".format(field)
