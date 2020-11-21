from flask_simplelogin import SimpleLogin, login_required


def verify_login(user):
  return user.get("username") == "admin" and user.get("password") == "123"


def init_app(app):
    SimpleLogin(app, login_checker=verify_login)