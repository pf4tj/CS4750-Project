from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from FFDB.models import Matchup
from DB_Access.forms import SearchMatchupFromTeamForm, SearchPlayersFromTeamForm

import json
import datetime
import pytz
from django.utils import timezone
import re


def HomePageView(request):
    return render(request, 'index.html')

def SearchMatchupFromTeam(request):
    if request.method == 'POST':
        form = SearchMatchupFromTeamForm(request.POST)
        if form.is_valid():
            return redirect('HomePageView')
    else:
        form = SearchMatchupFromTeamForm()
    return render(request, 'QT1.html', {'form': form})

def SearchPlayersFromTeam(request):
    if request.method == 'POST':
        form = SearchPlayersFromTeamForm(request.POST)
        if form.is_valid():
            return redirect('HomePageView')
    else:
        form = SearchPlayersFromTeamForm()
    return render(request, 'QT2.html', {'form': form})

def AddOrRemovePlayerFromTeam(request):
    return render(request, 'QT3.html')

class QT4(TemplateView):
    template_name = "QT4.html"

def PlayersWithoutTeam(request):
    return render(request, 'PlayersWithoutTeam.html')