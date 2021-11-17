from application import app, db
from application.models import Items
from flask import redirect, url_for

@app.route('/')
def home():
    return "Welcome to a basic todo app"