from django.test import TestCase
from django.urls import reverse
from core.models import User


class ViewsTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username="admin", email="admin@test.com", password="admin123")
        self.user = User.objects.create_user(username="user", email="user@test.com", password="user123")

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_apply_success_view(self):
        response = self.client.get(reverse('application_success'))
        self.assertEqual(response.status_code, 200)

    def test_admin_dashboard_access_for_admin(self):
        self.client.login(username="admin", password="admin123")
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_admin_dashboard_access_for_normal_user_denied(self):
        self.client.login(username="user", password="user123")
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 403)
