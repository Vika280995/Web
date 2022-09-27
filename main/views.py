from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models  import Task


from . forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    answers = Task.objects.all()
    return render (request,'index.html',{'title':'Главная страница','tasks':tasks,'answers': answers})

def about(request):
    return render(request,'about.html')

def create(request):
    error =""
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            Return , redirect = ('home')
        else:
            error = 'Форма была не верной'
    form = TaskForm()
    context ={
        'form': form,
        'error': error,
    }
    return render(request,'create.html',context)

def new_page(request):
    return render(request,'new_page.html')


