from django.db import models

from datetime import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
COLOR_CHOICES = (
    ('admin','admin'),
    ('employer', 'employer'),
    ('users','users'),
    ('finance','finance'),
    ('visitor','visitor'),
)
type = models.CharField(max_length=32,choices=COLOR_CHOICES,null=True)
type.contribute_to_class(User, 'type')
