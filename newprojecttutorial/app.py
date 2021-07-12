from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import redirect
from flask import url_for

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def home():
    return 'a welcome message'
@app.route('/capital/<string:capme>') 
def capitilize(capme): 
    return capme.upper()

@app.route('/about')
def about():
    return 'about page'

@app.route('/greetme/<string:name>')
def names(name):
    if name.lower() == 'ollie':
        return redirect(url_for('home'))
    else:
        return f'<h1 style="color:blue;font-size:46px;">Hey {name} hope you are well.</h1>'

@app.route('/name/<string:name>/<int:max>')
def repeatname(name, max):
    result = []
    for i in range (0, max):
        result.append(name)
    if max >= 5:
        return redirect(url_for('home'))
    return str(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')