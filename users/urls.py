from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
from . import views_ajax

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html', next_page='/'),
        name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path('ajax_signup/', views_ajax.ajax_signup, name='ajax_signup'),
]
