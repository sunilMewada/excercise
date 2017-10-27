from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from excercise.wsgi import application
from polls.models import Excercise


def index(request):
    return render (request, 'polls/index.html')


def anonymous(request):
    return render (request, 'polls/anonymous.html')


def restricted(request):
    latest_excercise_list = Excercise.objects.order_by ('application')[:100]
    context = {'latest_excercise_list': latest_excercise_list}
    return render (request, 'polls/restricted.html', context)