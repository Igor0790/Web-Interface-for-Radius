from django.contrib.auth import views
from django.views import generic

from apps.app_users.forms import AdminRadiusForm
from apps.app_users.models import AdminsRadiusModel


class RegistrationView(generic.CreateView):
    model = AdminsRadiusModel
    form_class = AdminRadiusForm
    template_name = 'app_users/templates/app_users/userregister.html'
    queryset = AdminsRadiusModel.objects.all()
    success_url = '/'


class LogoutView(views.LogoutView):
    template_name = 'app_users/templates/app_users/logout.html'
    next_page = '/'

class LoginView(views.LoginView):
    template_name = 'app_users/templates/app_users/login.html'
    next_page = '/'



