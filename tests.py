import unittest
from datetime import datetime, timedelta
from flask import url_for
from app import create_app, db, bcrypt
from app.models import User, CollectionPoint, Article, EnvironmentalData, EnvironmentalNews

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Create test app with testing configuration
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def create_test_user(self):
        """Helper method to create a test user"""
        hashed_password = bcrypt.generate_password_hash('testpassword').decode('utf-8')
        user = User(
            prenom='Test',
            nom='User',
            email='test@example.com',
            password=hashed_password,
            points=0,
            organic_waste=0,
            inorganic_waste=0
        )
        db.session.add(user)
        db.session.commit()
        return user

    def login(self, email='test@example.com', password='testpassword'):
        """Helper method to login"""
        return self.client.post('/auth/auth', data={
            'login': True,
            'email': email,
            'password': password
        }, follow_redirects=True)

    # Test Models
    def test_user_model(self):
        """Test User model"""
        user = self.create_test_user()
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.prenom, 'Test')
        self.assertEqual(user.nom, 'User')
        self.assertEqual(user.points, 0)
        self.assertEqual(user.organic_waste, 0)
        self.assertEqual(user.inorganic_waste, 0)

    def test_collection_point_model(self):
        """Test CollectionPoint model"""
        point = CollectionPoint(
            nom='Test Point',
            adresse='123 Test St',
            horaire='9-5',
            latitude=48.8566,
            longitude=2.3522,
            type_dechet='recyclable',
            date_collecte=datetime.now()
        )
        db.session.add(point)
        db.session.commit()

        retrieved_point = CollectionPoint.query.first()
        self.assertEqual(retrieved_point.nom, 'Test Point')
        self.assertEqual(retrieved_point.type_dechet, 'recyclable')

    # Test Authentication
    def test_registration(self):
        """Test user registration"""
        response = self.client.post('/auth/auth', data={
            'register': True,
            'prenom': 'New',
            'nom': 'User',
            'email': 'new@example.com',
            'telephone': '1234567890',
            'password': 'password123',
            'confirm_password': 'password123'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        user = User.query.filter_by(email='new@example.com').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.prenom, 'New')

    def test_login_logout(self):
        """Test login and logout functionality"""
        self.create_test_user()
        
        # Test login
        response = self.login()
        self.assertEqual(response.status_code, 200)
        
        # Test logout
        response = self.client.get('/auth/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Test Routes
    def test_home_route(self):
        """Test home route"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)  # Should redirect to auth

    def test_dashboard_route(self):
        """Test dashboard route with authentication"""
        self.create_test_user()
        self.login()
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)

    def test_blog_route(self):
        """Test blog route"""
        # Create test article
        article = Article(
            titre='Test Article',
            contenu='Test Content',
            image_url='test.jpg',
            source='test'
        )
        db.session.add(article)
        db.session.commit()

        response = self.client.get('/blog')
        self.assertEqual(response.status_code, 200)

    def test_get_collection_points_api(self):
        """Test collection points API"""
        self.create_test_user()
        self.login()
        
        # Create test collection point
        point = CollectionPoint(
            nom='Test Point',
            adresse='123 Test St',
            horaire='9-5',
            latitude=48.8566,
            longitude=2.3522,
            type_dechet='recyclable',
            date_collecte=datetime.now()
        )
        db.session.add(point)
        db.session.commit()

        response = self.client.get('/get_collection_points')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Test Point')

    # Test Forms
    def test_login_form_validation(self):
        """Test login form validation"""
        response = self.client.post('/auth/auth', data={
            'login': True,
            'email': 'invalid',  # Invalid email format
            'password': 'test'
        })
        self.assertIn(b'Adresse email invalide', response.data)

    def test_registration_form_validation(self):
        """Test registration form validation"""
        # Test password mismatch
        with self.client as c:
            response = c.post('/auth/auth', data={
                'register': True,
                'prenom': 'Test',
                'nom': 'User',
                'email': 'test@example.com',
                'password': 'password123',
                'confirm_password': 'different',
                'telephone': '1234567890'
            }, follow_redirects=True)
            
            # Check if the form validation failed and we're still on the registration page
            self.assertEqual(response.status_code, 200)
            # Verify we can still see the registration form
            self.assertIn(b'Sign Up', response.data)
            # The form should not process successfully with mismatched passwords
            user = User.query.filter_by(email='test@example.com').first()
            self.assertIsNone(user)

    def test_duplicate_email_registration(self):
        """Test registration with duplicate email"""
        # First create a user
        self.create_test_user()
        
        # Try to register another user with the same email
        with self.client as c:
            response = c.post('/auth/auth', data={
                'register': True,
                'prenom': 'Another',
                'nom': 'User',
                'email': 'test@example.com',  # Same email as test user
                'password': 'password123',
                'confirm_password': 'password123',
                'telephone': '1234567890'
            }, follow_redirects=True)
            
            # Verify the registration failed
            self.assertEqual(response.status_code, 200)
            # Check that we only have one user with this email
            users = User.query.filter_by(email='test@example.com').all()
            self.assertEqual(len(users), 1)
            # Verify the original user's details haven't changed
            self.assertEqual(users[0].prenom, 'Test')

if __name__ == '__main__':
    unittest.main()