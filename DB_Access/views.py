from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from FFDB.models import Matchup
from DB_Access.forms import SearchMatchupFromTeamForm, SearchPlayersFromTeamForm
from django.contrib.auth import login, authenticate, logout
from django.middleware.csrf import get_token

import json
import datetime
import pytz
from django.utils import timezone
import re

from .forms import SignUpForm

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

def logout_user(request):
    logout(request)
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print('okay')
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            rawPassword = form.cleaned_data.get('password')
            user = authenticate(request, username=username,
                                password=rawPassword)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

