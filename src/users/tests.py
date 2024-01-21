from django.test import TestCase
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="testuser1", email="test1@example.com", password="testpassword1")
        User.objects.create_user(username="testuser2", email="test2@example.com", password="testpassword2")

    def test_user_username(self):
        """Usernames are correctly identified"""
        user1 = User.objects.get(username="testuser1")
        user2 = User.objects.get(username="testuser2")
        self.assertEqual(user1.username, 'testuser1')
        self.assertEqual(user2.username, 'testuser2')

    def test_user_email(self):
        """Emails are correctly identified"""
        user1 = User.objects.get(email="test1@example.com")
        user2 = User.objects.get(email="test2@example.com")
        self.assertEqual(user1.email, 'test1@example.com')
        self.assertEqual(user2.email, 'test2@example.com')