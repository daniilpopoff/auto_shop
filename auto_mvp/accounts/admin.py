from django.contrib import admin

# Register your models here.
from .models import User, Customer, Admin

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Admin)