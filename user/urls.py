from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import CustomLoginView, RegisterView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('reg/', RegisterView.as_view(), name='reg'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
