from django import forms
from .models import *


class Category_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ERP_Form(forms.ModelForm):
    class Meta:
        model = Item
        # fields = ['title','contents','tags','image']
        exclude = ('active', 'status')
        # fields = '__all__'
