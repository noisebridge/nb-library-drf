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
    openlibrary_olid = models.CharField(max_length=255)
    openlibrary_description = models.TextField()


