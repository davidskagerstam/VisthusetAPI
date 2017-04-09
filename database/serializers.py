'''
Created on 25 dec. 2016

@author: Adrian
'''
from rest_framework.serializers import ModelSerializer

from database.models import BikeBooking, Booking

class BookingSerializer(ModelSerializer):
    
    class Meta:
        model = Booking 
        fields = ['booking_date', ]
        
class GuestUserSerializer(ModelSerializer):
    pass

class BikeExtraSerializer(ModelSerializer):
    pass 

    #class Meta:
        #model = BikeExtraBooking
        #fields = []
    
class BikeBookingList(ModelSerializer):
    person = BookingSerializer(required=True)
    extras = BikeExtraSerializer(required=False)
    class Meta:
        model = BikeBooking
        fields = ['booking_date', 'start_date', 'end_date', ]