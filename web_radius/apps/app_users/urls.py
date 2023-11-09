from django.urls import path
from apps.app_users import views

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]


# from django.conf.urls.defaults import patterns, url
#
# from app_users.forms import RADIUSAuthenticationForm
#
# urlpatterns = patterns('django.contrib.auth.views',
#
# url(r'^login/$', 'login',
# {'authentication_form': RADIUSAuthenticationForm},
# name='radius_login'),
#
# )