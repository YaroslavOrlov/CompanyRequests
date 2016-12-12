from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView, ContextMixin
from django.views.generic.list import ListView
from requests.models import UserProfile, Role
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView


class UsersListView(ListView):
    template_name = "account/users.html"
    model = UserProfile
    paginator_by = 10

    def get(self, request, *args, **kwargs):
        return super(UsersListView, self).get(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = "1"
        return context

    def get_queryset(self):
        return UserProfile.objects.all()


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