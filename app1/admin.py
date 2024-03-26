from django.contrib import admin

# Register your models here.
from .models import login
class Loginadmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number', 'password')
admin.site.register(login, Loginadmin)
