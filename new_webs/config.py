import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:ycc962464@127.0.0.1:3306/tests'
    SQLALCHEMY_COMMIT_ON_TEARDOWN =True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    