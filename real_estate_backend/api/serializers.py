from django.db import models
from rest_framework import serializers

# from django.contrib.auth.models import User, Group
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['name', 'password', 'email', 'phone']

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
