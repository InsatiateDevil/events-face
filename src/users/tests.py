from functools import partial

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class TestLoginCase(APITestCase):
    login_url = reverse("users:login")
    refresh_token_url = reverse("users:token_refresh")
    logout_url = reverse("users:logout")

    username = "test@user.com"
    password = "kah2ie3urh4k"

    def setUp(self):
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )

    def _login(self):
        data = {"username": self.username, "password": self.password}
        r = self.client.post(self.login_url, data)
        body = r.json()
        if "access" in body:
            self.client.credentials(HTTP_AUTHORIZATION="Bearer %s" % body["access"])
        return r.status_code, body

    def test_logout_response_200(self):
        _, body = self._login()
        data = {"refresh": body["refresh"]}
        r = self.client.post(self.logout_url, data)
        body = r.content
        self.assertEqual(r.status_code, 204)
        self.assertFalse(body, body)

    def test_logout_with_bad_refresh_token_response_400(self):
        self._login()
        data = {"refresh": "dsf.sdfsdf.sdf"}
        r = self.client.post(self.logout_url, data)
        body = r.json()
        self.assertEqual(r.status_code, 400)
        self.assertTrue(body, body)

    def test_logout_refresh_token_in_blacklist(self):
        _, body = self._login()
        r = self.client.post(self.logout_url, body)
        token = partial(RefreshToken, body["refresh"])
        self.assertRaises(TokenError, token)
