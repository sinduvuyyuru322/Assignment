from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('',create),
    path('post/', Postdetails, name='Postdetails'),
    path('get/', getbooks, name='getbooks'),
    path('update/',updatebooks, name='updatebooks'),
    path('delete',deletebook,name = 'deletebook'),


]

