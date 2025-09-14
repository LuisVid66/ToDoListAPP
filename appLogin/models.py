from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UsuarioSinEmailManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class UsuarioSinEmail(AbstractUser):
    email = None  # Eliminamos el campo email
    objects = UsuarioSinEmailManager()  # Usamos nuestro manager personalizado

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []  # No pedimos nada extra

    def __str__(self):
        return self.username