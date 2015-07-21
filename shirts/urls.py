from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^shirts/', views.listing, name='listing'),
    url(r'^shirt/(?P<pk>\d+)/', views.detail, name='detail'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^$', views.home, name='home'),
]