from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, nickname, password,  **extra_fields):
        if not nickname:
            raise ValueError('Пошта повинна бути заповнена')
        user = self.model(nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, nickname, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(nickname, password, **extra_fields)

    def create_superuser(self, nickname, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser повинен мати поле is_superuser = True')

        return self._create_user(nickname, password, **extra_fields)