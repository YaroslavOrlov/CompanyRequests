from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView, ContextMixin
from django.views.generic.list import ListView
from requests.models import UserProfile, Role, Department
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class UsersListView(ListView):
    model = UserProfile
    template_name = "account/users.html"
    paginator_by = 10

    def get(self, request, *args, **kwargs):
        return super(UsersListView, self).get(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context["departments"] = Department.objects.order_by("name")
        context["roles"] = Role.objects.order_by("name")
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = "1"
        return context

    def get_queryset(self):
        try:
            role_id = self.request.GET['role_id']
        except:
            role_id = 'all'
        try:
            department_id = self.request.GET['department_id']
        except:
            department_id = 'all'

        if (role_id == 'all' and department_id == 'all'):
            return UserProfile.objects.all();
        if (role_id == 'all' and department_id != 'all'):
            object_list = UserProfile.objects.filter(department = department_id)
        elif(role_id != 'all' and department_id == 'all'):
            object_list = UserProfile.objects.filter(role = role_id)
        else:
            object_list = UserProfile.objects.filter(department = department_id, role = role_id)
        return object_list


class CreateUserView(CreateView):
    model = User
    fields = ["username", "password", "first_name", "last_name", "email", "is_superuser", "is_staff", "is_active"]
    template_name = "account/user_add.html"
    success_url = "accounts"
   
    def form_valid(self, form):
        form.instance.password = make_password(form.cleaned_data["password"])
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("accounts")
        return super().post(request, *args, **kwargs)  
     

class CreateUserProfileView(CreateView):
    model = UserProfile
    fields = ["user", "department", "position", "role"]
    template_name = "account/user_profile_add.html"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("accounts")
        return super().post(request, *args, **kwargs)  

class UpdateUserProfile(UpdateView):
    model = UserProfile
    fields = ["user", "department", "position", "role"]
    template_name = "account/user_profile_edit.html"
    pk_url_kwarg = "user_id"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("accounts")
        return super().post(request, *args, **kwargs)  

class DeleteUserProfile(DeleteView):
    model = UserProfile
    template_name = "account/user_profile_delete.html"
    pk_url_kwarg = "user_id"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("accounts")
        return super().post(request, *args, **kwargs) 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["profile"] = UserProfile.objects.get(pk = self.kwargs["user_id"])
        return context;
