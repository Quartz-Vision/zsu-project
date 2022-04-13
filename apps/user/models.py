from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.common.models import UUIDModel


class User(AbstractUser, UUIDModel):
    pass