from django.contrib import admin
from .models import Category, MyDebts, OthersDebts, Notification

# Register your models here.

admin.site.register(Category)
admin.site.register(MyDebts)
admin.site.register(OthersDebts)
admin.site.register(Notification)
