from django import forms
from .models import Category, MyDebts, OthersDebts, Currency
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.core.exceptions import ValidationError

CURRENCIES = [('UAN', 'UAN'), ('USD', 'USD'), ('EUR', 'EUR')]


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name', 'the_limit', 'currently_spent', 'date_of_rent', 'due_date','currency', 'color_save']
        widgets = {
            'cat_name': forms.TextInput(attrs={'placeholder': 'Enter category name', 'class': 'input-text'}),
            'the_limit': forms.NumberInput(attrs={'placeholder': '0', 'class':'input-text', 'type':"text", 'id':"limit"}),
            'currently_spent': forms.NumberInput(attrs={'placeholder': '0', 'class':"input-text", 'type':"text", 'id':"spent"}),
            'date_of_rent': forms.DateInput(attrs={'type': 'date','id':'start-date', 'class': 'input-text'}),
            'due_date': forms.DateInput(attrs={'type': 'date','id':'end-date', 'class': 'input-text'}),
            'currency': forms.Select(choices=CURRENCIES, attrs={'class': 'custom-dropdown', 'id':'currency'}),
            'color_save': forms.TextInput(attrs={'type':"color", 'id':"bg-color", 'style':"width: 3px; height: 3px; border-radius: 360px"})
        }

    def clean_the_limit(self):
        data = self.cleaned_data['the_limit']
        if not self.is_editing:  
            if data <= 0 or not isinstance(data,int):
                raise ValidationError('Invalid data, must be more or equal zero and be integer')
        return data
    
    def clean_currently_spent(self):
        data = self.cleaned_data['currently_spent']
        if not self.is_editing:  
            if data < 0 or not isinstance(data,int):
                raise ValidationError('Invalid data, must be more than zero and be integer')
        return data

    def clean_date_of_rent(self):
        data = self.cleaned_data['date_of_rent']
        if not self.is_editing:  
            if data < datetime.date.today():
                raise ValidationError('Invalid date - impossible to create until today')
        return data

    def clean_due_date(self):
        data = self.cleaned_data['due_date']
        if not self.is_editing:  
            if data < datetime.date.today():
                raise ValidationError('Invalid date - impossible to set due today')
        if data < self.cleaned_data['date_of_rent']:
                raise ValidationError('Invalid date - impossible to set due today')
        return data

    def __init__(self, *args, **kwargs):
        self.is_editing = kwargs.pop('is_editing', False)  # Add this line
        self.request = kwargs.pop('request', None)
        super(CategoryCreateForm, self).__init__(*args, **kwargs)
        self.fields['date_of_rent'].initial = datetime.date.today()
        self.fields['color_save'].initial = "#b097da"

    def clean(self):
        cleaned_data = super(CategoryCreateForm, self).clean()
        cleaned_data['user'] = self.request.user  
        return cleaned_data
    

class MyDebtsCreateForm(forms.ModelForm):
    class Meta:
        model = MyDebts
        fields = ['debt_amount', 'currency', 'date_of_borrowing', 'debt_repayment_date', 'creditor_name']
        widgets = {
            'debt_amount': forms.NumberInput(attrs={'id': 'my-debt-amount'}),
            'currency': forms.Select(choices=Currency.choices, attrs={'class': 'custom-dropdown',
                                                                      'id': 'my-debt-currency'}),
            'date_of_borrowing': forms.DateInput(attrs={'type': 'date', 'id': 'my-debt-date-of-borrowing',
                                                        'required': True}),
            'debt_repayment_date': forms.DateInput(attrs={'type': 'date', 'id': 'my-debt-repayment-date'}),
            'creditor_name': forms.TextInput(attrs={'placeholder': 'Enter creditors name',
                                                    'id': 'my-debt-creditor-name'})
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(MyDebtsCreateForm, self).__init__(*args, **kwargs)

    def clean_debt_amount(self):
        debt_amount = self.cleaned_data.get('debt_amount')
        if debt_amount <= 0:
            raise forms.ValidationError('The amount of debt must be greater than zero')
        return debt_amount

    def clean(self):
        cleaned_data = super(MyDebtsCreateForm, self).clean()
        cleaned_data['user'] = self.request.user
        return cleaned_data


class OthersDebtsCreateForm(forms.ModelForm):
    class Meta:
        model = OthersDebts
        fields = ['debt_amount', 'currency', 'date_of_borrowing', 'debt_repayment_date', 'debtor_name']
        widgets = {
            'debt_amount': forms.NumberInput(attrs={'placeholder': '0', 'id': 'others-debt-amount'}),
            'currency': forms.Select(choices=Currency.choices, attrs={'class': 'custom-dropdown',
                                                                      'id': 'others-debt-currency'}),
            'date_of_borrowing': forms.DateInput(attrs={'type': 'date',
                                                        'id': 'others-debt-date-of-borrowing',
                                                        'required': True}),
            'debt_repayment_date': forms.DateInput(attrs={'type': 'date', 'id': 'others-debt-repayment-date'}),
            'creditor_name': forms.TextInput(attrs={'placeholder': 'Enter debtors name',
                                                    'id': 'others-debt-creditor-name'})
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(OthersDebtsCreateForm, self).__init__(*args, **kwargs)

    def clean_debt_amount(self):
        debt_amount = self.cleaned_data.get('debt_amount')
        if debt_amount <= 0:
            raise forms.ValidationError('The amount of debt must be greater than zero')
        return debt_amount

    def clean(self):
        cleaned_data = super(OthersDebtsCreateForm, self).clean()
        cleaned_data['user'] = self.request.user
        return cleaned_data

