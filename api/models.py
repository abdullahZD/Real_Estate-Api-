from django.db import models
from accounts.models import User


#Bulding Model
class Bulding(models.Model):
    property_type_choices = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        ('townhouse', 'Townhouse'),
        ('land', 'Land'),
        ('commercial', 'Commercial'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=property_type_choices)
    price = models.FloatField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    location = models.CharField(max_length=200)
    rooms = models.CharField(max_length=200)
    notes = models.TextField(blank=False, null=True)

    def __str__(self):
        return self.type


#Uplaod image mode
class BuldingImage(models.Model):
    building = models.ForeignKey(Bulding, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='bulding_images/')
    def __str__(self):
        return self.building.type


#Contact Model
class RequestBulding(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    bulding_location = models.CharField(max_length=100, blank=False)
    contract_duration = models.CharField(max_length=100)
    contract_type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


#Contact Us
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name




    
