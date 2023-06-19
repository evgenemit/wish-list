from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomUser


class LoginForm(AuthenticationForm):
    """Форма входа"""

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control text-center',
            'placeholder': 'Имя пользователя',
            'id': 'username',
            'autocomplete': 'off',
            'autocapitalize': 'none',
        })
    )
    password = forms.CharField(
        strip=True,
        widget=forms.widgets.PasswordInput(render_value=True, attrs={
            'class': 'form-control text-center',
            'placeholder': 'Пароль',
            'id': 'password',
            'autocomplete': 'off',
            'autocapitalize': 'none',
        })
    )


class RegisterForm(UserCreationForm):
    """Регистрация"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs = {
            'class': 'form-control text-center',
            'autocomplete': 'off',
            'placeholder': 'Пароль',
            'id': 'password1',
            'autocapitalize': 'none',
        }
        self.fields['password2'].widget.attrs = {
            'class': 'form-control text-center',
            'autocomplete': 'off',
            'placeholder': 'Подтвердите пароль',
            'id': 'password2',
            'autocapitalize': 'none',
        }

    class Meta:
        model = CustomUser
        fields = ('username', )

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control text-center',
                'id': 'username',
                'autocomplete': 'off',
                'placeholder': 'Имя пользователя',
                'autocapitalize': 'none',
            }),
        }
