# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Feeds(models.Model):
    
    url = models.URLField(max_length=300),
    created_time = models.TimeField(auto_now=False, auto_now_add=False)
    updated_time = models.TimeField(auto_now=True) 
    title = models.TextField() 
    feed = models.TextField()


