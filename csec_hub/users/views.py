from audioop import reverse
from pyexpat import model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

# View
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

# Mixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Model
from .forms import UserRegisterForm

# Email Verification 
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
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
        return redirect('users:email-sent')


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
        return redirect('users:link-expired')

def emailSent(request):
    return render(request,'email-sent.html',context={})

def expiredLink(request):
    return render(request,'link-expired.html',context={})

# Sign in view
class SignInView(LoginView):
    template_name = 'signin.html'
    redirect_authenticated_user = False
    extra_context = {'title': 'Sign In'}
    success_url = reverse_lazy('login')
    
# django sign out view
class SignOutView(LogoutView):
    template_name = 'logout.html'
    extra_context = {'title': 'Sign Out'}


# profile view
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user-profile.html'
    extra_context = {'title': 'Profile'}
    model = User

# profile update view
# class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
#     template_name = 'profile_update.html'
#     extra_context = {'title': 'Profile Update'}
#     success_message = "Your profile was updated successfully"


# password reset view
class PasswordResetView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    success_url = reverse_lazy('password_reset_done')
    success_message = "Password reset email sent successfully"
    # email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    extra_email_context = {'url': 'https://www.csec.org.in/hub/password_reset/{uid}/{token}'}

# password reset done view
class PasswordResetDoneView(SuccessMessageMixin, PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'
    success_message = "Password reset email sent successfully"




 # django class based view profile update view render multiple forms
class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'profile_update.html'
    extra_context = {'title': 'Profile Update'}
    form_class = UserRegisterForm
    success_message = "Your profile was updated successfully"
    success_url = reverse_lazy('profile')

    class Meta:
        model = User
        fields = ['username','first_name','last_name']

