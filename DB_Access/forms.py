from django import forms
from FFDB.models import Matchup, Team, Player, Our_User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SearchMatchupFromTeamForm(forms.Form):
    team_name = forms.ModelChoiceField(queryset=Team.objects.all())

class SearchPlayersFromTeamForm(forms.Form):
    team_name = forms.ModelChoiceField(queryset=Team.objects.all())

class RemovePlayerFromTeamForm(forms.Form):
    player_name = forms.ModelChoiceField(queryset=Player.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(RemovePlayerFromTeamForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['player_name'].queryset = Player.objects.filter(league_team=Team.objects.get(owner=Our_User.objects.get(user=user)))

class StartPlayerOnTeamForm(forms.Form):
    player_name = forms.ModelChoiceField(queryset=Player.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(StartPlayerOnTeamForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['player_name'].queryset = Player.objects.filter(league_team=Team.objects.get(owner=Our_User.objects.get(user=user)))

class BenchPlayerOnTeamForm(forms.Form):
    player_name = forms.ModelChoiceField(queryset=Player.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(BenchPlayerOnTeamForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['player_name'].queryset = Player.objects.filter(league_team=Team.objects.get(owner=Our_User.objects.get(user=user)))

class AddPlayerToTeamForm(forms.Form):
    player_name = forms.ModelChoiceField(queryset=Player.objects.filter(league_team=None))

class SignUpForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
