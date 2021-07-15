from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TaskForm(FlaskForm):
    name = StringField('Enter a task')
    submit = SubmitField('submit')