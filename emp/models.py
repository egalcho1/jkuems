from django.db import models

from datetime import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
COLOR_CHOICES = (
    ('admin','admin'),
    ('manager', 'manager'),
    ('employer', 'employer'),
    ('users','users'),
    ('finance','finance'),
    ('visitor','visitor'),
)
#types = [('employee','employee'),('visitor','visitor')]
type = models.CharField(max_length=32,choices=COLOR_CHOICES,null=True)
type.contribute_to_class(User, 'type')
class Request(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    rsever=models.CharField(max_length=255,null=True)
    dt=models.DateTimeField(auto_now_add=True)
    msg=models.TextField(null=True)
    answer=models.TextField(null=True)
    msga=models.TextField(null=True)
    dt=models.DateTimeField(auto_now=True)
