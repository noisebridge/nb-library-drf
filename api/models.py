# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    ''' Represents a title in the Noisebridge system

    
    In a sqlite database, the CharField max_length is 255
    https://docs.djangoproject.com/en/1.11/ref/databases/#notes-on-specific-fields

     
    '''
    
    # do we need to say a max length?
    id = models.IntegerField(primary_key=True)
    isbn = models.CharField(max_length=20)
    olid = models.CharField(max_length=20)
    lccn = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publish_date = models.CharField(max_length=30)
    number_of_pages = models.CharField(max_length=10)
    subjects = models.CharField(max_length=5000)
    openlibrary_medcover_url = models.CharField(max_length=500)
    openlibrary_preview_url = models.CharField(max_length=500)
    openlibrary_description = models.TextField(default=None)
    dewey_decimal_class = models.CharField(max_length=50)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, default=None)


class Location(models.Model):
    ''' Locations have a shortname and a pkey ID. 
    Books are linked to location by ForeignKey using the ID (pkey).
    '''
    id = models.IntegerField(primary_key=True)
    label_name = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    # books = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, blank=True)
