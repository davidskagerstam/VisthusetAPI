from django.db import models
from django.db.models.fields import CharField, DateField
from django.db.models.fields.files import ImageField

class Event(models.Model):
    Title = CharField(max_length=100)
    Description = CharField(max_length=500)
    Text = CharField(max_length=2000)
    Image = ImageField(upload_to='static/cafe/images')
    Start = DateField()
    End = DateField()
    Pub_date = DateField()
    Pub_end = DateField()
        
    def __str__(self):
        return self.Title