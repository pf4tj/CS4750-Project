from django import forms
from FFDB.models import Matchup, Team

class SearchMatchupFromTeamForm(forms.Form):
    team_name = forms.ModelChoiceField(queryset=Team.objects.all())

class SearchPlayersFromTeamForm(forms.Form):
    team_name = forms.ModelChoiceField(queryset=Team.objects.all())
