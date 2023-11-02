from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'CUSTOMER'),
        (2, 'AGENT'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    pass


class AgencyUser(AbstractUser):
    pass