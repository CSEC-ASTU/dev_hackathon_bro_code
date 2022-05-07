from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 
                    'first_name', 'last_name', 
                    'password1', 'password2', 
                    'phone', 'telegram_username', 
                    'sex', 'profile_picture'
                    ]
            