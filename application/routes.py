from application import app, db
from application.forms import ItemEntry
from application.models import Items
from flask import redirect, url_for, render_template
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def home():
    form = ItemEntry()
    items = Items.query.all()
    if len(items) == 0:
        return "Welcome to a basic todo app. Why not add some todos?"
    else:
        out = []
        for item in items:
            out.append( ''.join(str(item.id) + '||' + item.name + '||' + item.desc + '||' + item.status + '||' + str(item.date)))
        #return  out
        return render_template("home.html", items=out, form=form)


# Route to create a todo item
@app.route('/add/<name>/<desc>')
def add_item(name, desc):
    newitem = Items(name=name.lower(), desc=desc)
    db.session.add(newitem)
    db.session.commit()
    return "Added item"

# Routes to update an existing todo item
@app.route('/status/<int:id>/<status>')
def update_status(id, status):
    item = Items.query.get(id)
    item.status = status
    db.session.add(item)
    db.session.commit()
    return "Item status updated"

@app.route('/due/<int:id>/<date>')
def update_date(id, date):
    item = Items.query.get(id)
    item.date = datetime.strptime(date, '%Y-%m-%d')
    db.session.add(item)
    db.session.commit()
    return "Item date updated"

@app.route('/name/<int:id>/<name>')
def update_name(id, name):
    item = Items.query.get(id)
    item.name = name
    db.session.add(item)
    db.session.commit()
    return "Item name updated"

@app.route('/desc/<int:id>/<desc>')
def update_desc(id, desc):
    item = Items.query.get(id)
    item.desc = desc
    db.session.add(item)
    db.session.commit()
    return "Item description updated"

# Route to delete a todo item
@app.route('/delete/<int:id>')
def delete(id):
    db.session.delete(Items.query.get(id))
    db.session.commit()
    return "Item deleted"