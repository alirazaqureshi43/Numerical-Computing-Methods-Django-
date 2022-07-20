from typing import Text
from django import forms
from django.forms import TextInput, EmailInput

class FormName(forms.Form):
    val1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter 1st Value', 'style': 'width:450px;;', 'class': 'form-control' }))
    val2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter 2nd Value', 'style': 'width:450px;;', 'class': 'form-control'}))
    tol = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Tolerence', 'style': 'width:450px;;', 'class': 'form-control'}))
    stp = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Steps', 'style': 'width: 450px;', 'class': 'form-control'}))
    