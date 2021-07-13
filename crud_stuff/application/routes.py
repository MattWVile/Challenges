from application import app, db
from application.models import Games

@app.route('/add')
def add():
    new_game = Games(name='CyberFunk')
    db.session.add(new_game)
    db.session.commit()
    return 'Added new game'

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ''
    for game in all_games:
        games_string += '<br>' + game.name
        return games_string
    
@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name 
    db.session.commit()
    return first_game.name

@app.route('/delete/<game_name>')
def delete(game_name):
    entry_to_del = Games.query.filter_by(name = game_name).first()
    db.session.delete(entry_to_del)
    db.session.commit()
    return 'game deleted'


