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
	website_feed_url = models.URLField(null=True, max_length=300)
	website_url = models.URLField(null=True, max_length=300)
	website_title = models.TextField(null=True)
   	last_updated_on = models.DateTimeField(null=True, auto_now_add=False)

   	def __unicode__(self):
   		return str(self.feed_id) +' - '+str(self.website_title)

class FeedDetail(models.Model):
	feed_id = models.ForeignKey(FeedWebsite, related_name='feedW_feedD', null=True, on_delete=models.CASCADE)
	title = models.TextField(null=True)
	description = models.TextField(null=True)
	feed_link = models.URLField(null=True, max_length=300)
	published_on = models.DateTimeField(null=True, auto_now_add=False)

	def __unicode__(self):
		return str(self.feed_id)+' - '+str(self.feed_link)

class User_FeedWebsite(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	feed_id = models.ForeignKey(FeedWebsite, on_delete=models.CASCADE, null=True)
	# read = models.BooleanField(default=False)


