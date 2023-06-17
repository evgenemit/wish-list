from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token

from user.models import CustomUser


@login_required
def home(request):
    return render(request, 'wishlist/home.html')

def user_wishes(request, user_id: int):
    return render(request, 'wishlist/user_wishes.html', {'user_id': user_id})

@login_required
def add(request,):
    return render(request, 'wishlist/add.html')

@login_required
def profile(request):
    token = Token.objects.get_or_create(user=CustomUser.objects.get(pk=request.user.pk))
    return render(request, 'wishlist/profile.html', {'token': token[0]})
