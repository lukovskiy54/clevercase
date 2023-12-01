from django.contrib.auth.models import User
from django.db import models
from colorfield.fields import ColorWidget
from django import forms
import datetime
from django.utils import timezone


class Currency(models.TextChoices):
    UAH = '₴', '₴'
    EU = '€', '€'
    USD = '$', '$'


class Category(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    cat_name = models.CharField(max_length=30)
    the_limit = models.IntegerField(default=0)
    currently_spent = models.IntegerField(default=0)
    date_of_rent = models.DateField("Date of rent", default=timezone.now)
    currency = models.CharField(max_length=2, choices=Currency.choices, default=Currency.UAH)
    due_date = models.DateField("Due date")
    color_save = models.CharField(default="rgba(176,151,218,255)", max_length=100, blank=False)
    is_editing = False


    def __str__(self):
        return self.cat_name 


class MyDebts(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    debt_amount = models.IntegerField(default=0)
    currency = models.CharField(max_length=2, choices=Currency.choices, default=Currency.UAH)
    date_of_borrowing = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    debt_repayment_date = models.DateTimeField(null=True, blank=True)
    creditor_name = models.CharField(max_length=30)
    is_closed = models.BooleanField(default=False)


class OthersDebts(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    debt_amount = models.IntegerField(default=0)
    currency = models.CharField(max_length=2, choices=Currency.choices, default=Currency.UAH)
    date_of_borrowing = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    debt_repayment_date = models.DateTimeField(null=True, blank=True)
    debtor_name = models.CharField(max_length=30)
    is_closed = models.BooleanField(default=False)
