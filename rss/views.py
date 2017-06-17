
from django.http import Http404

from django.conf import settings
from django.shortcuts import render, redirect    
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from rss.models import FeedWebsite, User_FeedWebsite, FeedDetail
from django.contrib.auth.models import User
from django.urls import reverse
import json
from feedfinder import getFeeds

from feedly import feed_parser

def login(request):
    if request.user.is_authenticated:
        
        #check who is the user
        #retrive all the data for the user, that is (User.user_id = User_FeedWebsite.user_id & FeedWebsite.feed_id = User_FeedWebsite.feed_id)
        #website_title
        #
        return render(request,'feeds.html')

    return render(request,'login.html')

def feeds(request):
    if request.user.is_authenticated:
        return render(request,'feeds.html')
    else:
        return redirect('/')

#def add_subscription(request):
    #check who is the user
    #get the url
    
    #if url is there in db already then link the url to user
        #retrieve json data

    #else add url to FeedWebsite
        #call the parsing module
        #push into database
        #json.dump(data)
    #return the feeds and title

#def delete_subscription(request):
    # get the current
    # unsubscribe url for the user (delete the field of user and url combination in User_FeedWebsite)
    #return success

#def refresh_feeds(request):
    #for all the urls in feedurls refresh the database with newdata:
    #return done

#def display_feeds(request):
    #get the url 
    #check the database for feeds
    #return the feeds for the given url
#identify feed_id
def feed_id_identifier(url):
    obj = FeedWebsite.objects.filter()
    for item in obj:
        if url == item.website_feed_url:
            feed_id = item.feed_id
        else:
            feed_id = 0
    return feed_id


# def user_id_identifier(user):
#     print "current-user", user
#     obj = User.objects.filter()
#     for item in obj:
#         if str(user) == str(item.username):
#             user_id = str(item.id)
#             return user_id
#         else:
#             user_id = 0
#     return user_id


def checking_subscription(user_id,feed_id):
    obj = User_FeedWebsite.objects.filter()
    for item in obj:
        print user_id," --- ",item.user_id
        print feed_id,"------", item.feed_id_id
        if str(user_id) == str(item.user_id) and str(feed_id) == str(item.feed_id_id):
            return "yes"
    return "no"

def get_feeds(user_id, feed_id):
    obj = "lol"


def add_subscription(request):

    if request.method == 'POST':
        if request.user.is_authenticated:
           
            url_data = request.POST.get('url')

            #checking whether the link has feed content
            is_feed = getFeeds(url_data)
            if not is_feed:
                return HttpResponse('None')
            
            #check whether link exist in db
            Url_obj = FeedWebsite.objects.filter(website_feed_url=url_data)
            
            
            #if url_data not in db:
            if not Url_obj:
                #parse data
                data = feed_parser(url_data)
                website_title = data.website_title()
                website_feed_url = data.website_feed_link()
                website_url = data.website_original_link()
                last_updated_on = data.last_updated_on()
                feed_details = data.feed_details()
                                 
                
                FeedWebsite_Obj = FeedWebsite()
                FeedWebsite_Obj.website_title = website_title
                FeedWebsite_Obj.website_feed_url = website_feed_url
                FeedWebsite_Obj.website_url = website_url
                FeedWebsite_Obj.last_updated_on = last_updated_on
                
                FeedWebsite_Obj.save()
                f_id = FeedWebsite_Obj.feed_id

                for key, values in feed_details.items():
                    #insert into database

                    FeedDetail_Obj = FeedDetail(feed_id=FeedWebsite_Obj)
                    FeedDetail_Obj.title = key
                    FeedDetail_Obj.published_on = values[0]
                    FeedDetail_Obj.feed_link = values[1]
                    FeedDetail_Obj.description = values[2]
                    FeedDetail_Obj.save()
                    
                User_FeedWebsite_Obj = User_FeedWebsite()
                #refer intance of the table FeedWebsite_Obj
                User_FeedWebsite_Obj.feed_id = FeedWebsite_Obj
                User_FeedWebsite_Obj.user_id = request.user
                User_FeedWebsite_Obj.save()
            else:
                
                #check whether user has subscribed
                feed_id = feed_id_identifier(url_data)
                is_subscribed = checking_subscription(request.user,feed_id)
                
                if is_subscribed == "yes":
                    pass
                else:
                    s = "lol"

                #add user to the User_FeedWebsite table
                #get website title
                #get feed details for website
                #do query for data of the urls for the current user
        else:
            return HttpResponse('You are not logged in')

        return HttpResponse('Return data')
    else:
        return Http404()


#if facebook popup cancels then reload home page
def login_cancelled(request):
    return redirect('/')

#get everything from FeedWebsite

#get feed_id for the url


#get the current user's user_id
#for the user_id
#get if user_id matches the 