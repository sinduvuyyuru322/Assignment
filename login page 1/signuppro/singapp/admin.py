from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    # You can customize the admin panel fields here if needed

admin.site.register(User, CustomUserAdmin)
