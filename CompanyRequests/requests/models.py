from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    class Meta:
        db_table = "Departments"
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, verbose_name = "name")

    def __str__(self):
        return self.name

class Role(models.Model):
    class Meta:
        db_table = "Roles"
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, verbose_name = "name")

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        db_table = "Categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, verbose_name = "name")

    def __str__(self):
        return self.name

class LifeCycle(models.Model):
    class Meta:
        db_table = "Lifecycles"
        verbose_name = "Life cycle"
        verbose_name_plural = "Life cycles"

    id = models.AutoField(primary_key = True)
    opened = models.DateField(auto_now_add = True, verbose_name = "opened")
    distributed = models.DateField(null = True, verbose_name = "dustributed")
    proccesing = models.DateField(null = True, verbose_name = "proccesing")
    checking = models.DateField(null = True, verbose_name = "checking")
    closed = models.DateField(null = True, verbose_name = "closed")

    def __str__(self):
        return 'Request: {} '.format(self.id)


class UserProfile(models.Model):
    class Meta:
        db_table = "UserProfiles"
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    position = models.CharField(max_length = 50)
    department = models.ForeignKey(Department, null = True, on_delete = models.SET_NULL)
    role = models.ForeignKey(Role, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.user.username


class Activ(models.Model):
    class Meta:
        db_table = "Activs"
        verbose_name = "Activ"
        verbose_name_plural = "Activs"

    id = models.AutoField(primary_key = True)
    cub_number = models.CharField(max_length = 50, verbose_name = "cabinet number")
    department = models.ForeignKey(Department, null = True, on_delete = models.SET_NULL)
    
    def __str__(self):
        return self.cub_number

class Request(models.Model):
    class Meta:
        db_table = "Requests"
        verbose_name = "Request"
        verbose_name_plural = "Requests"

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, verbose_name = "name")
    description = models.CharField(max_length = 200, verbose_name = "description")
    comment = models.CharField(max_length = 200, verbose_name = "comment")
    status = models.IntegerField(verbose_name = "status")
    priority = models.IntegerField(verbose_name = "priority")
    activ = models.ForeignKey(Activ, null = True, on_delete = models.SET_NULL)
    category = models.ForeignKey(Category, null = True, on_delete = models.SET_NULL)
    user = models.ForeignKey(UserProfile, null = True, on_delete = models.SET_NULL)
    executor = models.IntegerField(null = True)
    lifecycle = models.ForeignKey(LifeCycle, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

