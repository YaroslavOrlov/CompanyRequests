from django.conf.urls import url
from requests import views
from requests import requestviews

urlpatterns = [
    url(r'^$', requestviews.RequestsListView.as_view(), name = 'requests'),
    url(r'^own/$', requestviews.UserRequestsListView.as_view(), name = 'requests_own'),
    url(r'^request/delete/(?:(?P<request_id>\d+)/)?$', requestviews.DeleteRequestView.as_view(), name = 'request_delete'),
    url(r'^request/detail/(?:(?P<request_id>\d+)/)?$', requestviews.DetailRequestView.as_view(), name = 'request_detail'),
    url(r'^request/executor/(?:(?P<executor_id>\d+)/)?$', requestviews.DetailExecutorView.as_view(), name = 'executor_detail'),
    url(r'^request/lifecycle/(?:(?P<lifecycle_id>\d+)/)?$', requestviews.DetailLifecycleView.as_view(), name = 'lifecycle_detail'),
    url(r'^request/add/$', requestviews.CreateRequestView.as_view(), name = 'request_add'),
]