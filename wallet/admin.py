from django.contrib import admin
from .models import Category, MyDebts, OthersDebts

# Register your models here.

admin.site.register(Category)
admin.site.register(MyDebts)
admin.site.register(OthersDebts)
