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


class AboutPageView(TemplateView):
    template_name = "about.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"

class SchedulerPageView(TemplateView):
    template_name = "scheduler.html"
