from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class RegisterViewTests(TestCase):
    def test_registration_creates_user_and_redirects(self):
        response = self.client.post(
            reverse('users:register'),
            {
                'username': 'newuser',
                'password1': 'SafePassword123!abc',
                'password2': 'SafePassword123!abc',
            },
        )

        self.assertRedirects(response, reverse('posts:list'))
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())

    def test_registration_form_is_available(self):
        response = self.client.get(reverse('users:register'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Register a New User')
