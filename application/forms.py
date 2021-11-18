from flask.app import Flask
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, DateField

class ItemEntry(FlaskForm):
    item_name = StringField('Name')
    item_desc = StringField('Description')
    item_stat = StringField('Status')
    item_date = DateField('Due Date')
    submit = SubmitField('Add')