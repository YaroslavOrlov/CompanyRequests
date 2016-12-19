from django.contrib import admin
from requests.models import Activ, Category, Department, LifeCycle, Request, Role, UserProfile

# Register your models here.

class LificycleAdmin(admin.ModelAdmin):
    fields = (('distributed', 'proccesing'), ('checking', 'closed'))

class UserProfileAdmin(admin.ModelAdmin):
    radio_fields = {"department": admin.HORIZONTAL}
    list_display = ('department', 'position')
    search_fields = ('department__name', 'position')


class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'priority', 'activ')
    list_filter = ('category', 'priority', 'activ')

class RequestInline(admin.StackedInline):
    model = Request

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        RequestInline,
    ] 

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class DepartmentAdmin(admin.ModelAdmin):
    inlines = [
        UserProfileInline,
    ]

admin.site.register(Activ)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(LifeCycle, LificycleAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Role)
admin.site.register(UserProfile, UserProfileAdmin)
