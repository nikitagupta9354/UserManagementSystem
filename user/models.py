from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=20, unique=True)
    billing_group = models.CharField(max_length=20, choices=[('free', 'Free'), ('pro', 'Pro'), ('premium', 'Premium')])

class Role(models.Model):
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True,default=None)

class MembershipRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    is_pending=models.CharField(max_length=10)