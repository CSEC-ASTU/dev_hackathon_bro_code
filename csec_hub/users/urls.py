from django.urls import path
from .views import SignInView, SignUpView, SignOutView, PasswordResetView, PasswordResetDoneView, activate,emailSent,expiredLink

app_name = 'users'


urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('register-user/', SignUpView.as_view(), name='register'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('email-sent', emailSent, name='email-sent'),
    path('link-expired', expiredLink, name='link-expired'),
    ]