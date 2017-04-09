from django.contrib import admin
from .models import Bike, Booking, BikeAvailable, BikesBooking, LunchBooking
from database.models import Damages, Facility, Rooms, Guest, RoomsBooking, Lunch
from Economy.models import Staff
from database.forms import BikesForm, LunchBookingForm
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# register bikes for users
class DamagesInline(admin.TabularInline):
    model = Damages
    extra = 1
    
@admin.register(Bike)
class BikesAdmin(admin.ModelAdmin):
    form_class = BikesForm
    list_display = ('number', 'attribute', 'wheelsize','rentOutCount', 'damage_report')
    
    readonly_fields = ['damage_report']
    inlines = (DamagesInline, )
    
    actions = ['reset_rent_out_count', ]  
    
    # Actions
    def reset_rent_out_count(self, request, queryset):
        queryset.update(rentOutCount = 0)
    reset_rent_out_count.short_description = 'Återställ antal uthyrningar till 0'

    # Readonly outputs
    def damage_report(self, instance):
        return format_html_join(mark_safe('<br/>'),
                                '{}',
                                ((line, ) for line in instance.damages.filter(repaired = 'False').all()
                                ) or mark_safe(
                                    "<span class='errors'>I can´t determine this adress</span>"))
    damage_report.short_description = 'Aktuella skador'

@admin.register(Damages)
class DamagesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['bike_id', 'discoveredDate', 'discoveredBy']}),
        ('Beskrivning', {'fields': ['damageType', ]}),
        ('Lagning',     {'fields': ['repaired', 'repairedBy', 'repairedDate'],
                         'classes': ['collapse', ]}),
        ]
    
    list_display = ['bike_id', 'discoveredDate', 'repaired', 'repairedDate', 'repairedBy']

@admin.register(BikeAvailable)
class BikesAvail(admin.ModelAdmin):
    fields = ['bike', 'available_date', 'available']



'''
Admins for rooms and facilities
'''
class RoomsInline(admin.TabularInline):
    model = Rooms
    extra = 0

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    # form = AccomodationForm
    fieldsets = [(None,      {'fields': ['name', 'organisation_number']}),
                 ('Kontaktuppgifter', {'fields': ['email', 'telephone', 'website']}),
                 ('Adress',  {'fields': ['adress', 'postCode', 'location']}),
                 ('Rum',     {'fields': ['rooms_report']}),
                 ('För hemsidan',   {'fields': ['slug']}),
                 ]
    list_display = ['name', 'email', 'telephone','website', 'adress_report', ]
    
    readonly_fields = ('adress_report', 'rooms_report')
    inlines = (RoomsInline, )
    
    def adress_report(self, instance):
        return format_html_join(
            mark_safe('<br/>'),
            '{}',
            ((line, ) for line in instance.get_full_adress()),
            ) or mark_safe("<span class='errors'>I can´t determine this adress</span>")
    adress_report.short_description = 'Adress'
    
    def rooms_report(self, instance):
        return format_html_join(mark_safe('<br/>'),
                                '{}',
                                ((line, ) for line in instance.rooms.all())
                                ) or mark_safe("<span class='errors'>Det finns inga registrerade rum hos denna anläggning</span>")

    rooms_report.short_description = 'Anläggningens rum'

@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['name', 'number', 'owned_by', 'standard']}),
        ('Specifikationer',     {'fields': ['max_guests', 'price']}),
        (None,          {'fields': ['describtion']}),
        ]
    
    list_display = ['name', 'owned_by', 'standard', 'max_guests', 'price', ]


'''
Admins for Lunch and Utilities

'''
@admin.register(Lunch)
class LunchAdmin(admin.ModelAdmin):
    fields = ['type', 'price' ,'slug'] 



'''
Booking admins

TODO:
# Gör funktion för att räkna ut totalpris
# Gör totalpris till readonly
# Beräkna subtotal i varje bokningsmodell

'''    
# Inlines
class RoomsBookingInLine(admin.TabularInline):
    model = RoomsBooking
    extra = 1
    fields = ['numberOfGuests', 'from_date', 'to_date', 'room', 'subtotal']
    readonly_fields = ['subtotal']
    
class BikesBookingInLine(admin.TabularInline):
    model = BikesBooking
    extra = 1
    
class LunchBookingInLine(admin.TabularInline):
    model = LunchBooking
    extra = 1
    fields = ['quantity', 'type', 'day', 'subtotal']
    readonly_fields = ['subtotal']
    
    
@admin.register(Booking)
class BookingsAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (None,          {'fields': ['guest', 'booking', 'created_at', 'updated_at']}),
        ('Info om gästen', {'fields': ['numberOfGuests', 'discount_code']}),
        ('Specifikationer', {'fields': ['total', 'booked_item_report']}),
        ]
    list_display = ['booking', 'guest', 'total', 'created_at', 'updated_at','numberOfGuests']
    readonly_fields = ['created_at', 'updated_at', 'booked_item_report', 'total']
    
    inlines = [BikesBookingInLine, RoomsBookingInLine, LunchBookingInLine]
    def booked_item_report(self, instance):
        return format_html_join(mark_safe('<br/>'),
                                '{}',
                                ((line, ) for line in instance.booked_item.all()
                                ) or mark_safe("<span class='errors'>Det finns inga objekt registrerade hos denna bokning</span>")
                                )
    booked_item_report.short_description = 'Enheter för denna bokning'
    
@admin.register(BikesBooking)
class BikesBookingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['booking', ]}),
        ('Pris',        {'fields': ['subtotal']}),
        ]
    
    def available_bikes(self, instance):
        # Gör funktion som hämtar alla lediga cyklar
        pass

@admin.register(RoomsBooking)
class RoomsBookingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['booking', 'numberOfGuests', 'room']}),
        ('datum',       {'fields': ['from_date', 'to_date']}),
        ('pris',        {'fields': ['subtotal']}),
        ]
    list_display = ['booking', 'numberOfGuests', 'room', 'subtotal','from_date', 'to_date']
    readonly_fields = ['subtotal']
    
    
@admin.register(LunchBooking)
class LunchBooking(admin.ModelAdmin):
    form = LunchBookingForm
    #fields = ['quantity', 'subtotal']
    


'''
Staff and guest admins. Belongs to auth app.
'''
class StaffAdmin(UserAdmin):
    pass
    
class GuestAdmin(StaffAdmin):
    pass


admin.site.unregister(User)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Guest, GuestAdmin)