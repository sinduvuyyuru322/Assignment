from django.urls import path,include
from .views import firstpage,homepage,login,create

urlpatterns = [
    path('',firstpage,name = 'firstpage'),
    path('homepage', homepage,name = 'homepage'),
    path("ad/",login),
    path('cre/',create,name = 'create'),
]