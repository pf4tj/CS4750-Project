from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from FFDB.models import Matchup, Player, Team, Our_User
from django.contrib.auth.models import User
from DB_Access.forms import SearchMatchupFromTeamForm, SearchPlayersFromTeamForm, AddPlayerToTeamForm, RemovePlayerFromTeamForm
from django.contrib.auth import login, authenticate, logout
from django.middleware.csrf import get_token
from django.contrib.auth.decorators import login_required

import json
import datetime
import pytz
from django.utils import timezone
import re

from .forms import SignUpForm

@login_required
def HomePageView(request):
    return render(request, 'index.html')

@login_required
def SearchMatchupFromTeam(request):
    if request.method == 'POST':
        form = SearchMatchupFromTeamForm(request.POST)
        if form.is_valid():
            return redirect('HomePageView')
    else:
        form = SearchMatchupFromTeamForm()
    return render(request, 'QT1.html', {'form': form})

@login_required
def SearchPlayersFromTeam(request):
    if request.method == 'POST':
        form = SearchPlayersFromTeamForm(request.POST)
        if form.is_valid():
            return redirect('HomePageView')
    else:
        form = SearchPlayersFromTeamForm()
    return render(request, 'QT2.html', {'form': form})

@login_required
def AddOrRemovePlayerFromTeam(request):
    if request.user.our_user.owns_team:
        return render(request, 'QT3.html', {'team':Player.objects.filter(league_team=Team.objects.get(owner=Our_User.objects.get(user=request.user)))})
    else:
        return redirect('NoTeam')

@login_required
def NoTeam(request):
    return render(request, 'NoTeam.html')

@login_required
def RemovePlayerFromTeam(request):
    if request.method == 'POST':
        form = RemovePlayerFromTeamForm(request.POST, user=request.user, )
        if form.is_valid():
            return redirect('QT3.html')
    else:
        form = RemovePlayerFromTeamForm(user=request.user)
    return render(request, 'RemovePlayer.html', {'form': form})

@login_required
def AddPlayerToTeam(request):
    if request.method == 'POST':
        form = AddPlayerToTeamForm(request.POST)
        if form.is_valid():
            return redirect('QT3.html')
    else:
        form = AddPlayerToTeamForm()
    return render(request, 'AddPlayer.html', {'form': form})

@login_required
def QT4(request):
    return render(request, 'QT4.html')

@login_required
def PlayersWithoutTeam(request):
    return render(request, 'PlayersWithoutTeam.html')

@login_required
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
