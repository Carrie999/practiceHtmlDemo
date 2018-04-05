CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

class Config():
    #coding=utf-8
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'Your secret key'
    # DB Config part
    DB_USERNAME = 'root'
    DB_PASSWORD = '123456'
    DB_SERVER = 'localhost'
    DB_NAME = 'blog'
    PER_PAGE = 2

    @staticmethod
    def init_app(app):
        pass