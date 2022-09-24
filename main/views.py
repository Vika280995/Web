from django.shortcuts import render
from django.http import HttpResponse
from .models  import Task

def index(request):
    tasks = Task.objects.order_by('-id')
    answers = Task.objects.all()
    return render (request,'index.html',{'title':'Главная страница','tasks':tasks,'answers': answers})

def about(request):
    return render(request,'about.html')

def create(request):
    return render(request,'create.html')

def new_page(request):
    return render(request,'new_page.html')


