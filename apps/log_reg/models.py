from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors= {}
        if len(postData['first-name']) < 2:
            errors['first-name'] = "First name should be at least 2 characters."
        if len(postData['last-name']) < 2:
            errors['last-name'] = "Name name should be at least 2 characters."
        if len(postData['email']) == 0:
            errors['email'] = "Email is required."
        if '@' not in postData['email']:
            errors['email'] = "Your email must include an '@' symbol."
        if '.' not in postData['email']:
            errors['email'] = "Your email must include a period '.'"
        if len(postData['password']) < 8:
            errors['email'] = "Password should be at least 8 characters."
        if postData['password'] != postData['confirm-pass']:
            errors['password'] = "Password does not match."
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors['email'] = "Email must be unique."
        return errors

    def login_validator(self, postData):
        errors = {}
        if len(postData['email']) == 0:
            errors['email'] = "Email is required."
        if len(postData['password']) == 0:
            errors['password'] = "Password is required."
        return errors

    def account_validator(self, postData):
        errors = {}
        if len(postData['first-name']) == 0:
            errors['first-name'] = "First name is required."
        if len(postData['last-name']) == 0:
            errors['last-name'] = "Last name is required."
        if len(postData['email']) == 0:
            errors['email'] = "Email is required."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"Id:{self.id}, First Name:{self.first_name}, Last Name:{self.last_name}, Email:{self.email}, Password:{self.password}"