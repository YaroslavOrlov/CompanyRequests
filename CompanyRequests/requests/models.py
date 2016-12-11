from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    class Meta:
        db_table = "Departments"

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)

class Role(models.Model):
    class Meta:
        db_table = "Roles"

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)

class Category(models.Model):
    class Meta:
        db_table = "Categories"

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)

class LifeCycle(models.Model):
    class Meta:
        db_table = "Lifecycles"

    id = models.AutoField(primary_key = True)
    opened = models.DateField()
    distributed = models.DateField(null = True)
    proccesing = models.DateField(null = True)
    checking = models.DateField(null = True)
    closed = models.DateField(null = True)


class UserProfile(models.Model):
    class Meta:
        db_table = "UserProfiles"

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    position = models.CharField(max_length = 50)
    department = models.ForeignKey(Department, null = True, on_delete = models.SET_NULL)
    role = models.ForeignKey(Role, on_delete = models.CASCADE)


class Activ(models.Model):
    class Meta:
        db_table = "Activs"

    id = models.AutoField(primary_key = True)
    cub_number = models.CharField(max_length = 50)
    department = models.ForeignKey(Department, null = True, on_delete = models.SET_NULL)

class Request(models.Model):
    class Meta:
        db_table = "Requests"

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    comment = models.CharField(max_length = 200)
    status = models.IntegerField()
    priority = models.IntegerField()
    activ = models.ForeignKey(Activ, null = True, on_delete = models.SET_NULL)
    category = models.ForeignKey(Category, null = True, on_delete = models.SET_NULL)
    user = models.ForeignKey(UserProfile, null = True, on_delete = models.SET_NULL)
    executor = models.IntegerField(null = True)
    lifecycle = models.ForeignKey(LifeCycle, on_delete = models.CASCADE)

