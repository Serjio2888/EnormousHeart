from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse

from heart.models import Event
from heart.forms import EventForm

def index(request):

    context = {	'name': 'admin'}
    return render(request, 'index.html', context)