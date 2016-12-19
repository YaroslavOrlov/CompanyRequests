from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView, ContextMixin
from django.views.generic.list import ListView
from requests.models import UserProfile, Role, Department
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator


class UsersListView(ListView):
    model = UserProfile
    template_name = "account/users.html"
    paginate_by = 1

    def get(self, request, *args, **kwargs):
        self.role_id = self.request.GET.get("role_id", 'all')
        self.department_id = self.request.GET.get("department_id", 'all')
        context = super(UsersListView, self).get(request, *args, **kwargs)
        return context
      
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
        object_list = UserProfile.objects.all()
        if (self.role_id != 'all'):
            object_list = object_list.filter(role = self.role_id)
        if (self.department_id != 'all'):
            object_list = object_list.filter(department = self.department_id)
        return object_list

@method_decorator(permission_required("request.user_profile.can_add_user"), name='dispatch')
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
     
@method_decorator(permission_required("request.user_profile.can_add_user_profile"), name='dispatch')
class CreateUserProfileView(CreateView):
    model = UserProfile
    fields = ["user", "department", "position", "role"]
    template_name = "account/user_profile_add.html"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("accounts")
        return super().post(request, *args, **kwargs)  

@method_decorator(permission_required("request.user_profile.can_change_user_proflle"), name='dispatch')
class UpdateUserProfile(UpdateView):
    model = UserProfile
    fields = ["user", "department", "position", "role"]
    template_name = "account/user_profile_edit.html"
    pk_url_kwarg = "user_id"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("accounts")
        return super().post(request, *args, **kwargs)  

@method_decorator(permission_required("request.user_profile.can_delete_user_proflle"), name='dispatch')
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
