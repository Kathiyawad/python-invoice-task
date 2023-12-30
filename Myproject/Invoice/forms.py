from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Model_Invoice
        fields = ['date','customername']
        widgets = {
            'date' : forms.DateInput(attrs={'class': "form-control", 'type': 'date', 'required':'true'}),
            'customername' : forms.TextInput(attrs={'class': 'form-control', 'maxLength': '50', 'required': 'true'})
        }

class InvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = Model_Invoice_Detail
        fields = ['description', 'quantity', 'unitprice', 'price']
        widgets = {
            'description': forms.Textarea(attrs={'class': "form-control", 'rows': 3}),
            'quantity': forms.NumberInput(attrs={'class': "form-control", "min": 0, 'required': 'true'}),
            'unitprice': forms.NumberInput(attrs={'class': "form-control", "min": 0, 'required': 'true'}),
            'price': forms.NumberInput(attrs={'class': "form-control", "readonly":"true"})
        }

