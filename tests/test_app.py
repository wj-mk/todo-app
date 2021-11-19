from flask import url_for
from flask_testing import  TestCase

from application import app, db
from application.models import Items
from application.forms import ItemEntry

# Create the base class
class TestBase(TestCase):
    def create_app(self):
        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()
        # Create entry
        test_todo = Items(name='test', desc='test')
        # Save todo to database
        db.session.add(test_todo)
        db.session.commit()
    
    # Will be called after every test
    def tearDown(self):
        # Claose the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()
                
# Test class to rest Read functionality
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test", response.data)
        self.assertIn(b"todo", response.data)
        self.assertNotIn(b'fake', response.data)
