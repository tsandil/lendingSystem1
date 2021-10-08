from django.conf.urls import url
from django.urls.conf import path
from . import views

app_name = 'sellItem'

urlpatterns = [
    url(r'^$', views.item_form, name='thirdpartyform'),
    # url(r'^$', views.item_confirm, name='itemadd'),
]