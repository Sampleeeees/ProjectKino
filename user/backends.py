from django.contrib.auth.backends import ModelBackend, UserModel

from .models import User


class CustomerBackend(ModelBackend):

    def authenticate(self, nickname=None, password=None, **kwargs):
        if nickname is None:
            nickname = kwargs.get(UserModel.USERNAME_FIELD)
        if nickname is None or password is None:
            return
        try:
            user = UserModel._default_manager.get_by_natural_key(nickname)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user


