from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^$', views.dummyindex, name='dummyindex'),
]