from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='searchcard'),
    url(r'^(?P<card_id>[0-9]+)/$', views.card_id, name='card_id'),
# below are tutorial test
    url(r'^byname/$', views.byname, name='byname'),
    url(r'^bynameresult/$', views.byname, name='bynameresult')
]
