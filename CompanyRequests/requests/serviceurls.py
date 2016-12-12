from django.conf.urls import url
from requests import views
from requests import serviceviews

urlpatterns = [
    url(r'^$', serviceviews.DepartmentListView.as_view(), name = 'services'),
    url(r'^department/add/$', serviceviews.CreateDepartmentView.as_view(), name = 'department_add'),
    url(r'^department/edit/(?:(?P<department_id>\d+)/)?$', serviceviews.UpdateDepartmentView.as_view(), name = 'department_edit'),
    url(r'^department/delete/(?:(?P<department_id>\d+)/)?$', serviceviews.DeleteDepartmentView.as_view(), name = 'department_delete'),
    url(r'^activs$', serviceviews.ActivListView.as_view(), name = 'activs'),
    url(r'^activ/add/$', serviceviews.CreateActivView.as_view(), name = 'activ_add'),
    url(r'^activ/edit/(?:(?P<activ_id>\d+)/)?$', serviceviews.UpdateActivView.as_view(), name = 'activ_edit'),
    url(r'^activ/delete/(?:(?P<activ_id>\d+)/)?$', serviceviews.DeleteActivView.as_view(), name = 'activ_delete'),
    url(r'^categories$', serviceviews.CategoryListView.as_view(), name = 'categories'),
    url(r'^category/add/$', serviceviews.CreateCategoryView.as_view(), name = 'category_add'),
    url(r'^category/edit/(?:(?P<category_id>\d+)/)?$', serviceviews.UpdateCategoryView.as_view(), name = 'category_edit'),
    url(r'^category/delete/(?:(?P<category_id>\d+)/)?$', serviceviews.DeleteCategoryView.as_view(), name = 'category_delete'),
]