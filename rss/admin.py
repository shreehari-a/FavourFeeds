#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from rss.models import FeedWebsite, FeedDetail, User_FeedWebsite
from django.contrib import admin

# Register your models here.
admin.site.register(FeedWebsite)
admin.site.register(FeedDetail)
admin.site.register(User_FeedWebsite)