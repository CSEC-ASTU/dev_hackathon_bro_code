# import model forms
from django import forms
from users.models import User
from .models import Voting, Subscription



class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False)

class VotingForm(forms.ModelForm):
    class Meta:
        model = Voting
        fields = ['msg']
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['tg_user_name']
    

    
		