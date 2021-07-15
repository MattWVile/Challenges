from flask_testing import TestCase
from flask import url_for

from application import app, db 
from application.models import Tasks

class TestBase(TestCase):
    def create_app(self ):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db'
        )

        return app

    def setUp(self):
        db.create_all()

        db.session.add(Tasks(name='run unit tests'))
        db.session.add(Tasks(name='do something else'))

        db.session.commit()

    def tearDown(self):
        db.drop_all()

class TestRead(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))

        assert 'run unit tests' in response.data.decode()
        assert 'do something else' in response.data.decode()