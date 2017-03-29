from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='searchcard'),
    # url(r'^$', views.index, name='index'),
    url(r'^(?P<card_id>[0-9]+)/$', views.card_id, name='card_id'),
]
