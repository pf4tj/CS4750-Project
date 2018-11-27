from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

import json
import datetime
import pytz
from django.utils import timezone
import re


def HomePageView(request):
    return render(request, 'index.html')


class QT1(TemplateView):
    template_name = "QT1.html"


class QT2(TemplateView):
    template_name = "QT2.html"

class QT3(TemplateView):
    template_name = "QT3.html"

class QT4(TemplateView):
    template_name = "QT4.html"