#from rss.serializers import FeedSerializer
from django.http import Http404
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status\
from django.shortcuts import render, redirect    
from django.http import HttpResponse
from django.views import View
from rss.models import Feeds
import json

# class FeedList(APIView):
#     """
#     List all snippets, or create a new snippet.

#     """
    
#     def get(self, request, format=None):
#         feeds = Feeds.objects.all()
#         serializer = FeedSerializer(feeds, many=True)
#         return Response('get request ', status=status.HTTP_201_CREATED)

#     def post(self, request, format=None):
#         serializer = FeedSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response('post request', status=status.HTTP_201_CREATED)
#         #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def login(request):
    return render(request,'login.html')

def feeds(request):
    session = 1
    return render(request,'feeds.html',{'session':session})

def addfeeds(request):
    print lol

def feedurls(request):
    feed = {'link':'narendramodi.in','title':'Modi is the guardian of India','description':'Narendra Damodardas Modi is an Indian politician who is the 14th and current Prime Minister of India, in office since May 2014. He was the Chief Minister of Gujarat from 2001 to 2014, and is the Member of Parliament for Varanasi.'}
    feed = json.dumps(feed)
    return render(request,'feeds.html',{'session':1,'feed':feed})