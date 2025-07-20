from django.test import TestCase
from core.forms import MemberApplicationForm
from core.models import Interest


class MemberFormTest(TestCase):
    def test_valid_form(self):
        interest = Interest.objects.create(name="Art")
        form_data = {
            "email": "test@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "phone": "9876543210",
            "location": "Leeds",
            "professional_background": "Artist",
            "why_join": "Inspiration",
            "how_contribute": "Workshops",
            "interests": [interest.id],
        }
        form = MemberApplicationForm(data=form_data)
        self.assertTrue(form.is_valid())
