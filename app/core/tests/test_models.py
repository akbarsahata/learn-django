from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email(self):
        """[SUCCESS] create user with email"""

        email = 'test@test.com'
        password = 'Pass123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_normalize_email(self):
        """[SUCCESS] email from input alway lowercased"""

        email = "test@TEST.com"

        user = get_user_model().objects.create_user(
            email=email
        )

        self.assertEqual(user.email, email.lower())

    def test_create_user_without_email(self):
        """[FAILED] create user without email"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'pass')
