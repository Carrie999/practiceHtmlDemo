from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__, instance_relative_config=True)
Bootstrap(app)

# app.config.from_object('config')
app.config.from_object('config')


from forum_app.views.admin_views.views import blue_admin
from forum_app.views.user_views.views import blue_user
app.register_blueprint(blue_admin, url_prefix='/admin')
app.register_blueprint(blue_user, url_prefix='/user')

#
from forum_app.views import views


