from django.db import models


class PropertyModel(models.Model):
    logo = models.ImageField(upload_to='images', blank=True)
    big_card_img = models.ImageField(upload_to='images', blank=True)
    card_01_img = models.ImageField(upload_to='images', blank=True)
    card_02_img = models.ImageField(upload_to='images', blank=True)
    card_03_img = models.ImageField(upload_to='images', blank=True)
    about_property = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=255, blank=True)
    option = models.CharField(max_length=255, blank=True)