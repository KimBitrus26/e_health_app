import os

#environment variable
basedir = os.path.abspath(os.path.dirname(__file__))

#configuration
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "myseckey12345"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" +  os.path.join(basedir, "database") 
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
