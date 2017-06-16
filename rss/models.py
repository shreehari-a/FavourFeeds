# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app_rssreader import settings
from django.contrib.auth.models import User
# Create your models here.



# rss_feed_id(pk)		feed_url	website_url		title_of_the_website
# class 
# rss_feed_id(fk)		userid(fk)
# rss_feed_id(fk)		title 		description 	feed_link

class FeedWebsite(models.Model):
	feed_id = models.AutoField(primary_key=True)
	website_feed_url = models.URLField(max_length=300)
	website_url = models.URLField(max_length=300)
	website_title = models.TextField()
        last_updated_on = models.DateTimeField(auto_now_add=False)

class FeedDetail(models.Model):
	feed_id = models.ForeignKey(FeedWebsite, on_delete=models.CASCADE)
	title = models.TextField()
	description = models.TextField()
	feed_link = models.URLField(max_length=300)
	published_on = models.DateTimeField(auto_now_add=False)

class User_FeedWebsite(models.Model):
	userid = models.ForeignKey(User, on_delete=models.CASCADE)
	feed_id = models.ForeignKey(FeedWebsite, on_delete=models.CASCADE)
	# read = models.BooleanField(default=False)

