from django.forms import ModelForm, Textarea, CharField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django import forms
from .models import *


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ExpensesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ExpensesForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(pk=self.request.user.id)
        self.initial['user'] = self.request.user
        self.fields['user'].widget = forms.HiddenInput()

    class Meta:
        model = Expenses
        fields = '__all__'
        widgets = {
            'user': forms.Select(attrs={'type':'hidden'}),
            'date_added': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'}),
        }
        error_messages = {
            'name': {
                'max_length': _("This Expense's name is too long."),
            },
        }
