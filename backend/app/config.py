import os 

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQL_DATABASE_URL = 'sqlite:///todo.db'
    SECRET_KEY = os.urandom(10)
    SESSION_COOKIE = "my_todo_app"
    