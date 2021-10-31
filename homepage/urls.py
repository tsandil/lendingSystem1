from django.urls import path

from .views import HomePageView, IndexView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url


app_name='homepage'
urlpatterns = [
    # path('', ItemListView.as_view(), name='index'),
    #  path('', views.index, name='index'),
    url(r'^$', IndexView.as_view(),name="home_list"),
    path('index', HomePageView.as_view(), name="Home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()

