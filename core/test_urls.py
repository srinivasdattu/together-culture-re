from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import HomePageView, AdminDashboardView


class URLTests(SimpleTestCase):
    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, HomePageView)

    def test_admin_dashboard_url(self):
        url = reverse('admin_dashboard')
        self.assertEqual(resolve(url).func.view_class, AdminDashboardView)
