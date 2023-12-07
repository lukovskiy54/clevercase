from django import forms
from .models import Regpay
import datetime
from django.core.exceptions import ValidationError

CURRENCIES = [('UAN', 'UAN'), ('USD', 'USD'), ('EUR', 'EUR')]
FREQ = [('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('Year', 'Year')]


class RegpayCreateForm(forms.ModelForm):
    class Meta:
        model = Regpay
        fields = ['reg_name', 'reg_date', 'amount', 'color_save', 'currency', 'frequency', 'frequency_int']
        widgets = {
            'reg_name': forms.TextInput(attrs={'placeholder': 'Enter regular pays name', 'class': 'input-text','style':'width:87.1%; margin-bottom:0;'}),
            'amount': forms.NumberInput(attrs={'placeholder': '0', 'class': 'input-text', 'type': "text", 'id': "amount",  'style':'margin-top:10px;'}),
            'reg_date': forms.DateInput(attrs={'type': 'date', 'id': 'reg-date', 'class': 'input-text', 'style':'width:87.1%;margin-top:16px; margin-bottom:30px'}),
            'color_save': forms.TextInput(attrs={'type': "color", 'id': "bg-color", 'style':"width: 100px; height: 50px;margin-left:53px; margin-top: 10px"}),
            'currency': forms.Select(choices=CURRENCIES, attrs={'class': 'custom-dropdown', 'id': 'currency'}),
            'frequency': forms.Select(choices=FREQ, attrs={'class' : 'custom-dropdown', 'id': 'frequency'}),
            'frequency_int': forms.NumberInput(attrs={'placeholder': '0', 'class': 'input-text', 'type': 'text', 'id': 'frequency_int'})
        }

    def clean_amount(self):
        data = self.cleaned_data['amount']
        if data <= 0 or not isinstance(data, int):
            raise ValidationError('Invalid data, must be more or equal zero and be integer')
        return data


    def clean_reg_date(self):
        data = self.cleaned_data['reg_date']
        if data < datetime.date.today():
            raise ValidationError('Invalid date - impossible to set due today')
        return data

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RegpayCreateForm, self).__init__(*args, **kwargs)
        self.fields['color_save'].initial = "#b097da"
        

    def clean(self):
        cleaned_data = super(RegpayCreateForm, self).clean()
        cleaned_data['user'] = self.request.user
        return cleaned_data
