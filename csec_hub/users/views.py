from django.urls import reverse_lazy
from .forms import UserRegisterForm

# View
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

# Mixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Sign up view
class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

# Sign in view
class SignInView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    extra_context = {'title': 'Sign In'}

# django sign out view
class SignOutView(LogoutView):
    template_name = 'users/logout.html'
    extra_context = {'title': 'Sign Out'}


# profile view
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
    extra_context = {'title': 'Profile'}

# profile update view
class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'users/profile_update.html'
    extra_context = {'title': 'Profile Update'}
    success_message = "Your profile was updated successfully"


# password reset view
class PasswordResetView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('password_reset_done')
    success_message = "Password reset email sent successfully"
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    extra_email_context = {'url': 'https://www.csec.org.in/hub/password_reset/{uid}/{token}'}

# password reset done view
class PasswordResetDoneView(SuccessMessageMixin, PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'
    success_message = "Password reset email sent successfully"




