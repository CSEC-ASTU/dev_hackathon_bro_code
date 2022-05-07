# import model forms
from django import forms
from users.models import User
from .models import Voting



class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False)



		