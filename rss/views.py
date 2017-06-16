#from rss.serializers import FeedSerializer
from django.http import Http404
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status\
from django.shortcuts import render, redirect    
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from django.urls import reverse
import json


def login(request):
    if request.user.is_authenticated:
       
        # return HttpResponseRedirect(reverse('addfeeds'))
        return redirect('/feeds')

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
    #for all the urls in feedurls refresh the database with newdata
    #return done

#def display_feeds(request):
    #get the url 
    #check the database for feeds
    #return the feeds for the given url

def feedurls(request):
    url_data = request.POST.get('url')

#     # url_data = request.POST['lol']
#     print url_data
#     return HttpResponse('yes done')
#     feed = {'link':'narendramodi.in','title':'Modi is the guardian of India','description':'as;ldfffffffffffffffffffajlkdjfkjsndjansdglkassndlkasndlkasmdflkasmdfla sdfasdflkasdv advkalkdmvlskdmlsdkglamglksfmglkssdmgmlskfnglksmglksfmglskdfglksgsfklga fglksmmfglksmfgl fglkasglaskmgl f lksdfgmlskfg sdflkgmsfmglkfglksmgklNarendra Damodardas Modi is an Indian politician who is the 14th and current Prime Minister of India, in office since May 2014. He was the Chief Minister of Gujarat from 2001 to 2014, and is the Member of Parliament for Varanasi.'}
#     feed = json.dumps(feed)
#     return render(request,'feeds.html',{'session':1,'feed':feed})

#if facebook popup cancels then reload home page
def login_cancelled(request):
    return redirect('/')

