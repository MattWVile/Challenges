from flask_testing import TestCase
from flask import url_for

from application import app, db 
from application.models import Tasks

class TestBase(TestCase):
    def create_app(self ):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            WTF_CSRF_ENABLED = False
        )

        return app

    def setUp(self):
        db.create_all()

        db.session.add(Tasks(name='run unit tests'))
        db.session.add(Tasks(name='do something else', done = True))

        db.session.commit()

    def tearDown(self):
        db.drop_all()

class TestRead(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))

        assert 'run unit tests' in response.data.decode()
        assert 'do something else' in response.data.decode()

    def test_read(self):
        response = self.client.get(url_for('read'))

        assert 'run unit tests' in response.data.decode()
        assert 'do something else' in response.data.decode()
    
class TestCreate(TestBase):
    def test_create(self):
        response = self.client.post(
            url_for('create'),
            data = {'name': 'Check create is working'},   
            follow_redirects=True   
            )

        assert "Check create is working" in response.data.decode()

class TestUpdate(TestBase):
    def test_update(self):
        response = self.client.post(
            url_for('update', id=1),
            data = {'name': 'Check update is working'},   
            follow_redirects=True   
            )

        assert "Check update is working" in response.data.decode()
        assert "do something else" in response.data.decode()
        assert 'run unit tests' not in response.data.decode()

    def test_complete(self):
        response = self.client.get(
            url_for('complete', id=1),   
            follow_redirects=True   
        )

        assert 'run unit tests - ✔️' in response.data.decode()
        assert 'do something else - ✔️' in response.data.decode()

    def test_uncomplete(self):
        response = self.client.get(
            url_for('uncomplete', id=2),   
            follow_redirects=True   
        )

        assert 'do something else - ❌' in response.data.decode()
        assert 'run unit tests - ❌' in response.data.decode()

class TestDelete(TestBase):
    def test_delete(self):
        response = self.client.get(
            url_for('delete', id=2),   
            follow_redirects=True   
        )
        assert "do something else" not in response.data.decode()
        assert 'run unit tests' in response.data.decode()

class TestViews(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)

    def test_create(self):
        response = self.client.get(url_for('create'))
        self.assert200(response)

    def test_update(self):
        response = self.client.get(url_for('update', id=1))
        self.assert200(response)