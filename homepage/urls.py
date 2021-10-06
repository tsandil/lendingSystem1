from django.urls import path

from homepage.views import HomePageView, ItemListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from homepage import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', ItemListView.as_view(), name='index'),
    # path('', views.index, name='index'),
    path('index', HomePageView.as_view(), name="Home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns+= staticfiles_urlpatterns()