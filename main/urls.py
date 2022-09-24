
from django.urls import path
from . import views
urlpatterns = [

    path('',views.index,name = 'home'),
    path('about',views.about, name ='about'),
    path('create',views.create, name ='create'),
    path('new_page',views.new_page,name= 'new_page'),

]