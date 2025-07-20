from django.test import TestCase
from core.models import User, Interest


class UserModelTest(TestCase):
    def test_create_user_with_fields(self):
        interest = Interest.objects.create(name="Tech")
        user = User.objects.create_user(
            username="test@example.com",
            email="test@example.com",
            password="pass1234",
            is_approved=True,
            phone="1234567890",
            location="London",
            professional_background="Engineer",
            why_join="To contribute",
            how_contribute="Tech mentoring"
        )
        user.interests.add(interest)
        self.assertTrue(user.is_approved)
        self.assertEqual(user.phone, "1234567890")
        self.assertIn(interest, user.interests.all())
