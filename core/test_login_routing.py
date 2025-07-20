from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginRedirectTest(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(
            username="admin@example.com",
            email="admin@example.com",
            password="adminpass",
            is_staff=True,
            is_superuser=True,
            is_active=True,
            is_approved=True
        )
        self.member_user = User.objects.create_user(
            username="member@example.com",
            email="member@example.com",
            password="memberpass",
            is_active=True,
            is_approved=True
        )

    def test_admin_login_redirects_to_dashboard(self):
        response = self.client.post(
            reverse("login"),
            {"username": "admin@example.com", "password": "adminpass"},
            follow=True
        )
        self.assertContains(response, "Admin Dashboard")
        self.assertEqual(response.request["PATH_INFO"], "/admin-dashboard/")

    # def test_member_login_redirects_to_comming_soon(self):
    #     response = self.client.post(
    #         reverse("login"),
    #         {"username": "member@example.com", "password": "memberpass"},
    #         follow=True
    #     )
    #     self.assertContains(response, "Coming Soon")
    #     self.assertEqual(response.request["PATH_INFO"], "/member-coming-soon/")
