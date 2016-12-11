from django.contrib import admin
from requests.models import Activ, Category, Department, LifeCycle, Request, Role, UserProfile

# Register your models here.


admin.site.register(Activ)
admin.site.register(Category)
admin.site.register(Department)
admin.site.register(LifeCycle)
admin.site.register(Request)
admin.site.register(Role)
admin.site.register(UserProfile)
