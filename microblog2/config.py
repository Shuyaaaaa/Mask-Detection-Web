import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'ECE1779'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Yxx19970910!@localhost:3306/ECE1779Asss'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 32 * 1024 * 1024
    UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif', '.jpeg', '.JPEG', '.PNG', '.JPG', '.GIF']
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'jianijiahappy@gmail.com'
    MAIL_PASSWORD = 'Jjn123456'
    ADMINS = ['jianijiahappy@gmail.com']




