from django.conf.urls import url
from requests import views
from requests import accountviews

urlpatterns = [
    url(r'^$', accountviews.UsersListView.as_view(), name = 'accounts'),
    url(r'^user/edit/(?:(?P<user_id>\d+)/)?$', accountviews.UpdateUserProfile.as_view(), name = 'user_edit'),
    url(r'^user/delete/(?:(?P<user_id>\d+)/)?$', accountviews.DeleteUserProfile.as_view(), name = 'user_delete'),
    url(r'^user/add/$', accountviews.CreateUserView.as_view(), name = 'user_add'),
    url(r'^user_profile/add/$', accountviews.CreateUserProfileView.as_view(), name = 'user_profile_add'),
]