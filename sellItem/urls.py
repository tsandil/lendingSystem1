from django.conf.urls import url
from . import views

app_name = 'sellItem'

urlpatterns = [
    url(r'^$',views.item_form, name='thirdpartyform')
]