from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm

class UserRegisterFormTest(TestCase):
    def test_user_register_form_valid(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'complex_password123',
            'password2': 'complex_password123'
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_register_form_invalid(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'complex_password123',
            'password2': 'different_password'
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

class UserUpdateFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='complex_password123')

    def test_user_update_form_valid(self):
        form_data = {'username': 'newuser', 'email': 'new@example.com'}
        form = UserUpdateForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())
