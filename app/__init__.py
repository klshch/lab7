#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.secret_key = b"secret"

app.config.from_object('config')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import views
