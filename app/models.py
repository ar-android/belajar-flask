from flask_login import UserMixin
from app import app, db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(60), index=True, unique=True)
  name = db.Column(db.String(255), index=True)
  password_hash = db.Column(db.String(128))
  is_admin = db.Column(db.Boolean)

  @property
  def password(self):
    """
    Prevent password from being accesed
    """
    return AttributeError("password is not readeble attribute.")

  @password.setter
  def password(self, password):
    """
    Set password to hassed password
    """
    self.password_hash = generate_password_hash(password)

  def verify_password(self, password):
    """
    Check if hashed password matched actual password
    """
    return check_password_hash(self.password_hash, password)

  def __repr__(self):
    return '<User {}>'.format(self.name)

@login_manager.user_loader
def load_user(id):
  return User.query.get(int(id))

