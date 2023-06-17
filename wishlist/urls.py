from django.urls import path

from .views import home, user_wishes, add, profile


urlpatterns = [
    path('', home, name='home'),
    path('@<int:user_id>/', user_wishes, name='user_wishes'),
    path('add/', add, name='add'),
    path('profile/', profile, name='profile'),
]
