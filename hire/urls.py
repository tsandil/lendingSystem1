from django.conf.urls import url
from django.urls.conf import path
from hire import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'hire'

urlpatterns = [
    url(r'^$', views.hire_form, name='hireform'),
    # path('', views.index1, name='hirePage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()




