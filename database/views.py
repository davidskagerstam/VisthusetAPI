from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import BikeAvailable, Booking
from calendar import calendar, HTMLCalendar
from django.views.generic.edit import CreateView
from datetime import datetime

def index(request):
    latest_booking_list = Booking.objects.order_by('-BookingDate')[:5]
    output = ', '.join([q.guest for q in latest_booking_list])
    return HttpResponse(output)

def ThanksView(request):
    return HttpResponse('Tack för din bokning!')

def booking(request, booking):
    response = "You're looking at booking %s."
    return HttpResponse(response % booking)

'''
class AccomodationBookingView(CreateView):
    form_class = AccomodationBookingForm
    template_name = './bookings/booking.html'

def BikeBookingView(request):    
    if request.method == 'POST':
        form = BikesBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/booking/thanks/')
    else:
        form = BikesBookingForm()
    return render(request, 'bookings/booking.html', {'form': form})

'''    
def perdelta(start, end, delta):
    curr = start
    while curr <= end:
        yield curr
        curr += delta
    
def trial(request):
    today = datetime.today()
    
    output = today.strftime(format)
    return HttpResponse(output)