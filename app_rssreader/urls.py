"""app_rssreader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rss import views
from django.contrib import admin

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$',views.login),
    url(r'^feeds/$', views.feeds),
    url(r'^add_subscription/$',views.add_subscription),
    url(r'^delete_subscription/$',views.delete_subscription),
    url(r'^feed_details/$',views.feed_details),
    url(r'^accounts/social/login/error/$', views.login_cancelled),
    
    url(r'^accounts/', include('allauth.urls')),

            ]

