from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from .forms import LoginForm, RegisterForm


class CustomLoginView(LoginView):
    """Вход"""

    template_name = 'user/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True


class RegisterView(CreateView):
    """Регистрация"""

    template_name = 'user/reg.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
