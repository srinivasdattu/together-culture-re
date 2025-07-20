from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse


def generate_password_reset_link(user, request):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    relative_url = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
    absolute_url = request.build_absolute_uri(relative_url)
    return absolute_url
