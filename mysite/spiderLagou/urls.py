from django.conf.urls import include, url
from spiderLagou import views

urlpatterns = [
    url(r'^$', views.test, name = 'test'),
]