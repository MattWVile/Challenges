from flask.templating import render_template
from application import app, db
from application.models import Tasks

from flask import redirect, url_for, request
from .forms import TaskForm
from .models import Tasks


@app.route('/')
def home():
    tasks =Tasks.query.all()
    return render_template("home.html", tasks=tasks)

@app.route('/create', methods=['GET', 'POST'])
def create(): 
    form = TaskForm()
    if request.method == 'POST':
        new_task = Tasks(name=form.name.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('create.html', form=form) 

@app.route('/read')
def read():
    all_tasks = Tasks.query.all()
    tasks_string = ''
    for task in all_tasks:
        tasks_string += '<br>' + task.name + ' ' +  str(task.done)
    return tasks_string
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Tasks.query.get(id)
    form = TaskForm()

    if request.method == 'POST':
        task.name = form.name.data
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('create.html', form=form) 

@app.route('/complete/<int:id>')
def complete(id):
    task = Tasks.query.get(id)
    task.done = True
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/uncomplete/<int:id>')
def uncomplete(id):
    task = Tasks.query.get(id)
    task.done = False
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
    entry_to_del = Tasks.query.get(id)
    db.session.delete(entry_to_del)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/completed')
def completed():
    all_tasks = Tasks.query.all()
    tasks_string = ''
    for task in all_tasks:
        if task.done == True:
            tasks_string += '<br>' + task.name + ' ' +  str(task.done)
    if len(tasks_string) >= 1:  
        return tasks_string
    else:
        return 'you lazy boi go complete tasks'

