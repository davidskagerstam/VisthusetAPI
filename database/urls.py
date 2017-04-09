'''
Created on 16 okt. 2016

@author: Adrian
'''
from django.conf.urls import url
from . import views

app_name = "database"
urlpatterns = [
    # /bookings/
    url(r'^$', views.index , name="index"),
    # /bookings/bookingNo/
    url(r'^(?P<booking_id>[0-9]+)/$', views.booking, name='booking'),
    #url(r'^accomodation/', views.AccomodationBookingView.as_view()),
    #url(r'^bikes/', views.BikeBookingView, name='bikebooking'),
    url(r'^thanks/', views.ThanksView, name= 'thanks'),
    url(r'^test/', views.trial),
    ]