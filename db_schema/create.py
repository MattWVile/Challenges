from app import db, Users

db.drop_all()
db.create_all()

testuser = Users(first_name = 'Bob', last_name = 'Smith')
db.session.add(testuser)
db.session.commit