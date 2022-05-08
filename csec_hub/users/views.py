from django.urls import reverse_lazy
from django.shortcuts import redirect, render

# View
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

# Mixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Membership, Excuitive

# Model
from .forms import UserRegisterForm

# Email Verification 
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token, executive_request_token
from django.core.mail import EmailMessage
from django.contrib.auth import login
from django.http import HttpResponse

# import get user model
from django.contrib.auth import get_user_model

User = get_user_model()


# Sign up view
class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your blog account.'
        message = render_to_string('account_activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        # check if the email exits
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('Please confirm your email address to complete the registration')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # reverse to login page
        return redirect('login')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def accept_request(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        membership = Membership.objects.filter(user=user).order_by('-id')[0]  
        excuitive = Excuitive.objects.get(user=membership)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and executive_request_token.check_token(user, token):
        excuitive.is_accepted = True
        excuitive.save()
        login(request, user)
        # reverse to login page
        print("accepted")
        return HttpResponse("You accepted the request!")
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def decline_request(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        membership = Membership.objects.filter(user=user).order_by('-id')[0]  
        excuitive = Excuitive.objects.get(user=membership)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and executive_request_token.check_token(user, token):
        excuitive.delete()
        # reverse to login page
        print("declined")
        return HttpResponse("You successfuly declined the request!")
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Decline link is invalid!')

# Sign in view
class SignInView(LoginView):
    template_name = 'login.html'
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


# django class based view profile update view render multiple forms
class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'users/profile_update.html'
    extra_context = {'title': 'Profile Update'}
    success_message = "Your profile was updated successfully"
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
    success_url = reverse_lazy('profile')
  
