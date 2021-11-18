from application import app, db
from application.models import Items
from flask import redirect, url_for

@app.route('/')
def home():
    items = Items.query.all()
    if len(items) == 0:
        return "Welcome to a basic todo app. Why not add some todos?"
    else:
        # don't understand how this works yet, but can move on
        out = ''
        for item in items:
            print(item)
            out += ''.join(str(item.id) + '||' + item.name + '||' + item.desc + '||' + item.status) + '<br>'
        return  out

@app.route('/add/<name>/<desc>')
def add_item(name, desc):
    newitem = Items(name=name.lower(), desc=desc)
    db.session.add(newitem)
    db.session.commit()
    return "Added item"
