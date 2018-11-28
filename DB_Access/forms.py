from django import forms
from FFDB.models import Matchup, Team
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SearchMatchupFromTeamForm(forms.Form):
    team_name = forms.ModelChoiceField(queryset=Team.objects.all())

class SearchPlayersFromTeamForm(forms.Form):
    team_name = forms.ModelChoiceField(queryset=Team.objects.all())

class SignUpForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')