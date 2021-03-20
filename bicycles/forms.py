from django import forms
from django.forms import ModelForm
from .models import Bike_type, Bike_brand, ProductBicycles

class Bike_typeForm(forms.ModelForm):
    title = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': "Name", 'required': "required"}))
    categories_bicycles = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': "Type", 'required': "required"}))
    is_visible = forms.BooleanField(widget=forms.CheckboxInput(attrs={'required':'required'}))

    class Meta(object):
        model = Bike_type
        fields = ('title', 'categories_bicycles', 'is_visible')

class Bike_brandForm(forms.ModelForm):
    title = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': "Name", 'required': "required"}))
    categories_bicycles = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': "Type", 'required': "required"}))
    is_visible = forms.BooleanField(widget=forms.CheckboxInput(attrs={'required':'required'}))

    class Meta(object):
        model = Bike_brand
        fields = ('title', 'categories_bicycles', 'is_visible')

class ProductBicyclesForm(forms.ModelForm):
    titel = forms.CharField(max_length=50,
                             widget=forms.TextInput(attrs={'placeholder': "Name", 'required': "required"}))
    titel_model = forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs={'placeholder': "Model number", 'required': "required"}))
    price = forms.DecimalField(max_digits=7, decimal_places=2,
                                widget=forms.NumberInput(attrs={'required': 'required'}))
    images = forms.ImageField(widget=forms.ClearableFileInput())
    bike_type = forms.ModelChoiceField(queryset=Bike_type.objects.all())
    bike_brand = forms.ModelChoiceField(queryset=Bike_brand.objects.all())
    description = forms.CharField(max_length=300,
                                  widget=forms.TextInput(
                                      attrs={'placeholder': "300 characters", 'required': "required"}))
    available = forms.BooleanField(required=True)
#    created = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])
#    updated = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])

    class Meta(object):
        model = ProductBicycles
        fields = ('titel', 'titel_model', 'price', 'images', 'bike_type', 'bike_brand', 'description', 'available')
