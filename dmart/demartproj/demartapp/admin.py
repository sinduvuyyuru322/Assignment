from django.contrib import admin

# Register your models here.
from .models import product_details,customer_details,Order
admin.site.register(product_details)
admin.site.register(customer_details)
admin.site.register(Order)