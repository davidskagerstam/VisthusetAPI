'''
Created on 9 nov. 2016

@author: Adrian
'''
from django import forms
from .models import Booking, Lunch
from database.models import BikeExtra, Bike, LunchBooking, BikesBooking
from .choices import Lunch_Choices
from django.forms.formsets import BaseFormSet

'''
TODO:
* Lägg in en kalender där det går att bläddra i bokningar
* Gör det möjligt att välja vilka cyklar som ska ingå i en bokning
'''
class BikesForm(forms.ModelForm):
    
    class Meta:
        model = Bike
        fields = ['number', 'bikeKeyNo', 'wheelsize', 'attribute', 'extra']
        
class BikeExtraForm(forms.ModelForm):
    class Meta:
        model = BikeExtra
        fields = ['name', 'number']

class BikeBookingForm(forms.ModelForm):
    class Meta:
        model = BikesBooking
        fields = ['subtotal']
        
        
class LunchBookingForm(forms.ModelForm):
    type = forms.ChoiceField(choices=Lunch_Choices)
    
    class Meta:
        model = LunchBooking
        fields = ['type', 'quantity', 'subtotal']
        help_texts = {'quantity': 'Hur många av den givna lunchen?'}
        label = {'quantity': 'kvantitet', 'subtotal': 'delsumma',
                 'type': 'Lunchtyp'}
        
