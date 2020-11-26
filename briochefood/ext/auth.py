from flask_simplelogin import SimpleLogin


def verify_login(user):
    return user.get("username") == "Django" and user.get("password") == "Livre"


def init_app(app):
    SimpleLogin(app, login_checker=verify_login)
