from django.urls import path,include
from .views import create,loginpage,logoutpage

urlpatterns = [
    path('',create),
    path('login/',loginpage,name = 'login'),
    path('logout/',logoutpage,name = 'logout'),
]
