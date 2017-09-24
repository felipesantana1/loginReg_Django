from __future__ import unicode_literals
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'[A-Z0-9]')

class UsersManager(models.Manager):

    def validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'Name field must contain at least 2 characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Name field must contain at least 2 characters'
        if len(postData['email']) < 1:
            errors['email'] =  'Must enter email addres'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email/password'
        if len(postData['password']) < 8:
            errors['password'] = 'password must contain more than 8 characters'
        if not PASSWORD_REGEX.match(postData['password']):
            errors['password'] = 'Invalid email/password'
        return errors

    def loginValidator(self, postData):
        errors = {}
        if postData['email'] < 1:
            errors['email'] = 'No email/password detected. Please try again.'
        if postData['password'] < 1:
            errors['password'] = 'No email/password detected. Please try again.'
        if not Users.objects.filter(email=postData['email']):
            errors['login'] = 'Invalid email/password. Please try again or register'
        elif not bcrypt.checkpw(postData['password'].encode(), Users.objects.get(email=postData['email']).password.encode()):
            errors['login'] = 'Invalid email/password. Please try again or register'
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()