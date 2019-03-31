from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse

from heart.models import Event, Task, Partner
from heart.forms import EventForm, TaskForm

from django.contrib.auth.models import User

import smtplib

def authenticate(username=None, password=None):
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            return None
        
      

class SponsView(DetailView):
    model = Partner
    template_name = 'spons.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partner'] = Partner.objects.all()
        context['ev'] = Event.objects.all()
        context['tasks'] = Task.objects.all()
        return context

def func(email, password):
    print('rofl')
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('moonheritage@gmail.com','serjio12')
    msg = 'Hello! Welcome to our site! Your password is '+password
    smtpObj.sendmail("moonheritage@gmail.com",email,msg)

def auth(reguest): 
    if reguest.POST:
        email = reguest.POST.get("email")
        password = reguest.POST.get("password")
        if '@' in email:
            func(email, password)
        user = authenticate(email,password)
        context = {}
        if user:
            context['event'] = Event.objects.get(id=1)
            context['partner'] = Partner.objects.all()
            context['ev'] = Event.objects.all()
            context['tasks'] = Task.objects.all()
            if user.groups.filter(name='Volonters').exists():
                context['type']='vol'
                return render(reguest, 'event.html', context)
            if user.groups.filter(name='Organizator').exists():
                context['type']='org'
                return render(reguest, 'event.html', context)
            else:
                context['type']='noob'
                return render(reguest, 'event.html', context)
            
    context = {}
    return render(reguest, 'auth.html', context)


        

def cabinet(reguest):
    return render(reguest,'cabinet.html',{})

#def index(request):

#    context = {	'ev': Event.objects.all(), 'name': 'admin'}
#    return render(request, 'index.html', context)

def event(request):
    if request.POST:
        print(request.POST)
    context = {	'name': 'admin'}
    return render(request, 'event.html', context)

class EventView(DetailView):
    model = Event
    template_name = 'event.html'
        
    def get_context_data(self, **kwargs):
        ev = Event.objects.all()
        context = super().get_context_data(**kwargs)
        context['notif'] = Notification.objects.all()
        context['partner'] = Partner.objects.all()
        context['ev'] = Event.objects.all()
        context['tasks'] = Task.objects.all()
        return context

class TaskAdd(CreateView):
    template_name = 'task_add.html'
    form_class = TaskForm


    def get_success_url(self):
        return ""