from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, DateField, DecimalField, SelectField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    age = IntegerField('Age')
    dob = DateField('Date of birth YYYY-MM-DD', format = '%Y-%m-%d')
    height = DecimalField('Height in meters')
    vaccinated = SelectField('Vaccinated', choices=[('Yes','Yes'),('no','no')])
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        age = form.age.data
        dob = form.dob.data
        height = form.height.data
        vaccinated = form.vaccinated.data
        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return 'thank_you ' + first_name + ' ' + last_name + ' you were born on ' + str(dob)

    return render_template('home.html', form=form, message=error)

@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')

@app.route('/list')
def list():
    users = ["ben", "harry", "bob", "jay", "matt", "bill"]
    return render_template('list.html', users=users)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')