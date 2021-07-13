from application import app, db
from application.models import Tasks

from flask import redirect, url_for

@app.route('/')
def home():
    tasks =Tasks.query.all()
    result =''
    for task in tasks:
        result += '<br>' + task.name
    return result
@app.route('/add/<task>')
def create(task):
    new_task = Tasks(name=task)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/read')
def read():
    all_tasks = Tasks.query.all()
    tasks_string = ''
    for task in all_tasks:
        tasks_string += '<br>' + task.name
    return tasks_string
    
# @app.route('/update/<description>')
# def update(description):
#     first_task = Tasks.query.first()
#     first_task.desc = description 
#     db.session.commit()
#     return first_task.name + '<br>' + first_task.desc 

# @app.route('/completed/')
# def isdone():
#     first_task = Tasks.query.first()
#     first_task.done = True
#     db.session.commit()
#     return 'task is done'

@app.route('/delete/<int:id>')
def delete(id):
    entry_to_del = Tasks.query.get(id)
    db.session.delete(entry_to_del)
    db.session.commit()
    return redirect(url_for('home'))


