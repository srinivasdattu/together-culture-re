from django import forms
from .models import User, Interest


class MemberApplicationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'location',
            'interests', 'professional_background', 'why_join', 'how_contribute'
        ]
        widgets = {
            'interests': forms.CheckboxSelectMultiple(),
        }
