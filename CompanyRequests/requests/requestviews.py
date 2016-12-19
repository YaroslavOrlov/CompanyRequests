from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView, ContextMixin
from django.views.generic.list import ListView
from requests.models import UserProfile, Role, Department, Request, LifeCycle
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from _datetime import datetime
from django.views.generic.detail import DetailView
from django.db.models.query_utils import Q
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator


class RequestsListView(ListView):
    model = Request
    template_name = "request/requests.html"
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        return super(RequestsListView, self).get(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
        context = super(RequestsListView, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = "1"
        return context

class UserRequestsListView(ListView):
    model = Request
    template_name = "request/own_requests.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(UserRequestsListView, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = "1"
        return context
    
    def get_queryset(self):
        user_profile = UserProfile.objects.get(user = self.request.user)
        return Request.objects.filter(user = user_profile)

@method_decorator(permission_required("request.request.can_add_request"), name='dispatch')
class CreateRequestView(CreateView):
    model = Request
    fields = ["name", "description", "priority", "activ", "category"]
    template_name = "request/request_add.html"
    success_url = "accounts"
   
    def form_valid(self, form):
        life_cycle = LifeCycle()
        life_cycle.save()
        user_profile = UserProfile.objects.get(pk = self.request.user)

        form.instance.status = 1
        form.instance.lifecycle = life_cycle
        form.instance.user = user_profile
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("accounts")
        return super().post(request, *args, **kwargs)  

class DetailRequestView(DetailView):
    model = Request
    template_name = "request/request_detail.html"
    pk_url_kwarg = "request_id"

class DetailExecutorView(DetailView):
    model = UserProfile
    template_name = "request/executor_detail.html"
    pk_url_kwarg = "executor_id"

class DetailLifecycleView(DetailView):
    model = LifeCycle
    template_name = "request/life_cycle_detail.html"
    pk_url_kwarg = "lifecycle_id"

class DeleteRequestView(DeleteView):
    model = Request
    template_name = "request/request_delete.html"
    pk_url_kwarg = "request_id"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("requests")
        return super().post(request, *args, **kwargs) 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["request"] = Request.objects.get(pk = self.kwargs["request_id"])
        return context;

     