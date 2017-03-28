from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='searchcard'),
    # url(r'^$', views.index, name='index'),
]
