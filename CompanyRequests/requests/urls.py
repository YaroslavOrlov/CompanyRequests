from django.conf.urls import url
from requests import views
from requests import accountviews

urlpatterns = [
    url(r'^$', accountviews.UsersListView.as_view(), name = 'accounts'),
    url(r'^user/edit/(?:(?P<user_id>\d+)/)?$', accountviews.UsersListView.as_view(), name = 'user_edit'),
    url(r'^user/delete/(?:(?P<user_id>\d+)/)?$', accountviews.UsersListView.as_view(), name = 'user_delete'),
    url(r'^user/add/$', accountviews.CreateUserView.as_view(), name = 'user_add'),
    #url(r'^(?:(?P<id>\d+)/)?$', views.products, name = 'products'),
    #url(r'^product/(?P<id>\d+)/$', views.product, name = 'product'),
]