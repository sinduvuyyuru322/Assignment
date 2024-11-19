
from django.urls import path,include
from .views import product,customer,create_order

urlpatterns = [
    path('',product),

    path('cus/',customer),
    path('create_order/', create_order, name='create_order'),
]