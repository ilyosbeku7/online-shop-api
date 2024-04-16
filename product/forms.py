from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        exlude=['id']

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        exlude=['id']