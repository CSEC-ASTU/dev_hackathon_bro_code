from django.urls import path, reverse_lazy
from .views import SignInView, SignUpView, SignOutView, PasswordResetView, PasswordResetDoneView, activate,emailSent,expiredLink,ProfileView,ProfileUpdateView

from django.contrib.auth import views as auth_views

app_name = 'users'


urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('profile/',ProfileView.as_view(), name='profile'),
    path('update-profile/',ProfileUpdateView.as_view(), name='update-profile'),
    path('register-user/', SignUpView.as_view(), name='register'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('email-sent', emailSent, name='email-sent'),
    path('link-expired', expiredLink, name='link-expired'),
    ]

urlpatterns += [
path(
        "change-password/",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/change_password.html",
            success_url="/auth/change-password/done",
        ),
        name="change_password",
    ),

    path(
        "change-password/done",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="registration/change_password_done.html",
        ),
        name="change_password_done",
    ),

    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="passwordReset/password_reset_form.html",
            
            
            # email_template_name="registration/password-reset/password_reset_email.html",
            success_url= reverse_lazy('users:email-sent')
        ),
        name="password_reset",
    ),

    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
        template_name="registration/password-reset/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="passwordReset/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password-reset/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    ]
