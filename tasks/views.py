from asyncio import tasks
from cProfile import label
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse



# Create your views here.

class NewTask(forms.Form):
    task= forms.CharField(label = "New Task")
   


def index(request):
    if "tasks" not in request.session:
        request.session['tasks']=[]


    return render (request, 'tasks/index.html' ,{'tasks': request.session["tasks"]})


def add(request):

 if request.method == 'POST':
    form= NewTask(request.POST)
    if form.is_valid():
        task = form.cleaned_data['task']
        request.session['tasks'] += [task]
        return HttpResponseRedirect(reverse("tasks:index"))
    else:
        return render(request,"tasks/add.html", {
        "form": form
    })

 return render(request,"tasks/add.html", {
        "form": NewTask()
    })