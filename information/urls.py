from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^list/', views.list,name='list'),
    url(r'^detail/', views.detail,name='detail'),
    url(r'^add/', views.add,name='add'),
    url(r'^audit$/', views.audit,name='audit'),
    url(r'^$', views.index,name='index'),
]