from django.test import TestCase, Client
from django.urls import reverse

class LoginValidationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')

    def test_login_page_renders_successfully(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'User Login')

    def test_valid_username(self):
        response = self.client.post(self.url, {
            'username': 'chetan123',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Input validation successful')

    def test_valid_username_with_underscore(self):
        response = self.client.post(self.url, {
            'username': 'chetan_123',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Input validation successful')

    def test_username_too_short(self):
        response = self.client.post(self.url, {
            'username': 'ab',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username')

    def test_username_starts_with_number(self):
        response = self.client.post(self.url, {
            'username': '123chetan',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username')

    def test_username_with_special_characters(self):
        response = self.client.post(self.url, {
            'username': 'chetan@123',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username')

    def test_password_too_short(self):
        response = self.client.post(self.url, {
            'username': 'chetan123',
            'password': 'abc123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Password must be at least 8 characters long.')

    def test_password_not_exposed_in_response(self):
        secret_password = 'secret_password_123'
        response = self.client.post(self.url, {
            'username': 'chetan123',
            'password': secret_password
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, secret_password)

