from django.shortcuts import render
from django.http import HttpResponse
from .models  import Task

def index(request):
    tasks = Task.objects.all()
    answers = Task.objects.all()
    return render (request,'index.html',{'title':'Главная страница','tasks':tasks,'answers': answers})

def about(request):
    return render(request,'about.html')


