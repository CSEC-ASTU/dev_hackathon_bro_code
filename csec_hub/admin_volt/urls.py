from django.urls import path
from . import views

app_name = 'admin'


urlpatterns = [
    path('register',views.register,name = 'register'),

]