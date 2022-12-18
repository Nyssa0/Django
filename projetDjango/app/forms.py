# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Product


# create a ModelForm
class ProductForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Product
        fields = "__all__"
