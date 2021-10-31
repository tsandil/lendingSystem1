from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url 

from users import views as user_views
from sellItem import views as sell_views
from hire import views as hire_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('home/',user_views.home, name='home'),
    path('signup/', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    url(r'^feedback_form/', include('form.urls')),
    path('feedback_form/', user_views.addlend, name='feedback'),
    url(r'^homepage/', include('homepage.urls')),
    path('homepage/', user_views.homePage, name='homepage'),
    url(r'^thirdpartyform/', include('sellItem.urls')),
    path('thirdpartyform/', sell_views.item_form, name='thirdpartyform'),
    url(r'^hireform/', include('hire.urls')),
    path('hireform/', hire_views.hire_form, name='hireform'),
    # url(r'^hirePage/', include('hire.urls')),
    # path('hirePage/', hire_views.hirePage, name='hirePage'),

]