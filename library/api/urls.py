from django.conf.urls import url
from library.api import views

urlpatterns = [
    url(r'^$', views.dummyindex, name='dummyindex'),
]