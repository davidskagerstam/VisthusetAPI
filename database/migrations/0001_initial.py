# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 21:26
from __future__ import unicode_literals

import database.models
import database.validators
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_guestuser_staff'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Economy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='Nummer')),
                ('bikeKeyNo', models.CharField(blank=True, max_length=15, verbose_name='Cykelnyckel')),
                ('rentOutCount', models.IntegerField(default=0, verbose_name='antal uthyrningar')),
                ('wheelsize', models.CharField(choices=[('large', '28"'), ('medium', '26"'), ('small', '22"')], max_length=10, verbose_name='Däckdiameter')),
                ('attribute', models.CharField(choices=[('vuxen', 'vuxen'), ('barn', 'barn')], max_length=10, verbose_name='vuxen/barn')),
                ('extra', models.CharField(blank=True, choices=[('child_seat', 'barnsadel'), ('bike_carriage', 'cykelkärra')], max_length=15, verbose_name='Knuten till tillbehör')),
            ],
            options={
                'ordering': ['-attribute', 'number'],
                'verbose_name': 'cykel',
                'verbose_name_plural': 'cyklar',
            },
        ),
        migrations.CreateModel(
            name='BikeAvailable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_date', models.DateField()),
                ('available', models.BooleanField(default=True)),
                ('bike', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='database.Bike')),
            ],
            options={
                'verbose_name': 'tillgänglighet cykel',
                'verbose_name_plural': 'tillgänglighet cyklar',
            },
        ),
        migrations.CreateModel(
            name='BikeExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('child_seat', 'barnsadel'), ('bike_carriage', 'cykelkärra')], max_length=10, verbose_name='cykeltillbehör')),
                ('number', models.PositiveIntegerField(default=None, verbose_name='Nummer')),
                ('attached_to', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bikeextra', to='database.Bike', verbose_name='knuten till cykel')),
            ],
        ),
        migrations.CreateModel(
            name='BikesBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking', models.PositiveIntegerField(default=database.models.calc_booking_no, primary_key=True, serialize=False, verbose_name='boknings id')),
                ('numberOfGuests', models.IntegerField(default=2, verbose_name='antal gäster')),
                ('special_requests', models.TextField(blank=True, max_length=255, verbose_name='övrigt')),
                ('preliminary', models.BooleanField(default=False, verbose_name='preliminär')),
                ('longest_prel', models.DateTimeField(blank=True, null=True, validators=[database.validators.validate_preliminary], verbose_name='längsta preliminärbokning')),
                ('start_date', models.DateField(null=True, verbose_name='datum för avresa')),
                ('end_date', models.DateField(null=True, verbose_name='datum för hemresa')),
                ('discount_code', models.CharField(blank=True, max_length=15, null=True, validators=[database.models.validate_discount_code], verbose_name='rabattkod')),
                ('checked_in', models.BooleanField(default=False, verbose_name='incheckad (J/N)')),
                ('checked_out', models.BooleanField(default=False, verbose_name='utcheckad(J/N)')),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('payed', models.BooleanField(default=False, verbose_name='betald')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Bokning',
                'verbose_name_plural': 'bokningar',
            },
        ),
        migrations.CreateModel(
            name='Damages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discoveredDate', models.DateField(default=datetime.date.today, verbose_name='Skada upptäckt')),
                ('repairedDate', models.DateField(blank=True, default=datetime.date.today, verbose_name='Skada reparerad')),
                ('damageType', models.TextField(max_length=200, verbose_name='beskrivning av skada')),
                ('repaired', models.BooleanField(default=False, verbose_name='lagad (J/N)')),
                ('bike_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='damages', to='database.Bike', verbose_name='Skada på cykel')),
                ('discoveredBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='discovered_by', to='Economy.Employee', verbose_name='upptäckt av')),
                ('repairedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repaired_by', to='Economy.Employee', verbose_name='lagad av')),
            ],
            options={
                'ordering': ['repaired', 'discoveredDate'],
                'verbose_name': 'skada',
                'verbose_name_plural': 'skador',
            },
        ),
        migrations.CreateModel(
            name='Discount_codes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, verbose_name='kod')),
                ('value', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='boendeanläggning')),
                ('organisation_number', models.CharField(blank=True, max_length=12)),
                ('telephone', models.CharField(blank=True, max_length=15, verbose_name='telefon')),
                ('email', models.EmailField(max_length=254, verbose_name='E-postadress')),
                ('website', models.URLField(blank=True, verbose_name='hemsida')),
                ('adress', models.CharField(blank=True, max_length=25, verbose_name='gatuadress')),
                ('postCode', models.CharField(blank=True, max_length=8, verbose_name='postkod')),
                ('location', models.CharField(blank=True, max_length=25, verbose_name='ort')),
                ('slug', models.SlugField(blank=True, default='')),
            ],
            options={
                'verbose_name': 'boendeanläggning',
                'verbose_name_plural': 'boendeanläggningar',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('newsletter', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'gäst',
                'verbose_name_plural': 'gäster',
            },
            bases=('auth.guestuser', models.Model),
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='')),
                ('type', models.CharField(choices=[('vegetarian', 'vegetarisk'), ('meat', 'kallskuret'), ('fish', 'Vätternröding')], default='vegetarian', max_length=15, verbose_name='lunchalternativ')),
                ('price', models.PositiveIntegerField(default=95, verbose_name='pris')),
            ],
            options={
                'verbose_name': 'lunch',
                'verbose_name_plural': 'luncher',
            },
        ),
        migrations.CreateModel(
            name='LunchBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('day', models.DateField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=8)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_lunches', to='database.Booking')),
                ('type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='database.Lunch')),
            ],
        ),
        migrations.CreateModel(
            name='PackageBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='namn')),
                ('number', models.PositiveIntegerField(blank=True)),
                ('describtion', models.TextField(blank=True, max_length=255, verbose_name='Beskrivning')),
                ('standard', models.CharField(choices=[('hotel', 'Hotell'), ('hote_budget', 'Hotell budget'), ('hostel', 'Vandrarhem')], max_length=20, verbose_name='standard')),
                ('max_guests', models.PositiveIntegerField(default=4, verbose_name='Max antal gäster')),
                ('price', models.DecimalField(decimal_places=2, default=0, help_text='Pris för rum exkl. moms', max_digits=7, verbose_name='pris exkl. moms')),
                ('owned_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='database.Facility', verbose_name='anläggning')),
            ],
            options={
                'ordering': ['owned_by'],
                'verbose_name': 'rum',
                'verbose_name_plural': 'rum',
            },
        ),
        migrations.CreateModel(
            name='RoomsAvailable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_date', models.DateField()),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoomsBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfGuests', models.PositiveIntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=8)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_rooms', to='database.Booking')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Rooms')),
            ],
        ),
        migrations.CreateModel(
            name='Utilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('describtion', models.TextField()),
                ('number', models.PositiveIntegerField()),
                ('brand', models.CharField(choices=[('LB', 'LunchBots'), ('CC', 'Clean Canteen')], max_length=5)),
            ],
            options={
                'verbose_name': 'tillbehör',
            },
        ),
        migrations.AddField(
            model_name='roomsavailable',
            name='bookings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='available_rooms', to='database.RoomsBooking'),
        ),
        migrations.AddField(
            model_name='roomsavailable',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='database.Rooms'),
        ),
        migrations.AddField(
            model_name='discount_codes',
            name='guest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='gäst'),
        ),
        migrations.AddField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest', to='database.Guest', verbose_name='gäst'),
        ),
        migrations.AddField(
            model_name='bikesbooking',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_bike', to='database.Booking'),
        ),
        migrations.AddField(
            model_name='bikeavailable',
            name='bookings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availableBike', to='database.BikesBooking'),
        ),
        migrations.AlterUniqueTogether(
            name='bike',
            unique_together=set([('number', 'attribute')]),
        ),
    ]
