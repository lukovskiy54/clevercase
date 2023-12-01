from django import forms
from .models import Regpay

CURRENCIES = [('UAN', 'UAN'), ('USD', 'USD'), ('EUR', 'EUR')]
FREQ = [('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('Year', 'Year')]


class RegpayCreateForm(forms.ModelForm):
    class Meta:
        model = Regpay
        fields = ['reg_name', 'reg_date', 'amount', 'color_save', 'currency', 'frequency', 'frequency_int']
        widgets = {
            'reg_name': forms.TextInput(attrs={'placeholder': 'Enter regular pays name', 'class': 'input-text'}),
            'amount': forms.NumberInput(attrs={'placeholder': '0', 'class': 'input-text', 'type': "text", 'id': "amount"}),
            'reg_date': forms.DateInput(attrs={'type': 'date', 'id': 'reg-date', 'class': 'input-text'}),
            'color_save': forms.TextInput(
                attrs={'type': "color", 'id': "bg-color", 'style': "width: 3px; height: 3px; border-radius: 360px"}),
            'currency': forms.Select(choices=CURRENCIES, attrs={'class': 'custom-dropdown', 'id': 'currency'}),
            'frequency': forms.Select(choices=FREQ, attrs={'class' : 'custom-dropdown', 'id': 'frequency'}),
            'frequency_int': forms.NumberInput(attrs={'placeholder': '0', 'class': 'input-text', 'type': 'text', 'id': 'frequency_int'})
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RegpayCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(RegpayCreateForm, self).clean()
        cleaned_data['user'] = self.request.user
        return cleaned_data
