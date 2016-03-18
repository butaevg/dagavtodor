from django.contrib.auth.backends import ModelBackend
from .models import DUser
from django.contrib.auth.models import User, check_password

default_app_config = "users.apps.UsersAppConfig"

class DUserBackend(ModelBackend):
    def authenticate(self, username = None, password = None, **kwargs):
        try:
            user = DUser.objects.get(username = username)
            if user.check_password(password):
                return user
        except DUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = DUser.objects.get(pk = user_id)
            if user.is_active:
                return user
            return None
        except DUser.DoesNotExist:
            return None