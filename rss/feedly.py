import re
import urllib2

class feed_parser:
    def __init__(self, url):

        self.url = url
        
        req = urllib2.Request(url, headers={'Content-type': 'text/xml'})
        r = urllib2.urlopen(req)
        self.response = r.read()

    def website_title(self):
        response = self.response
        try:
            website_title = re.findall('<title>.*?</title>', response)[0]
            website_title = re.sub(r'<title>','',website_title)
            website_title = re.sub(r'<\/title>','',website_title)
        except:
            website_title = 'No Title'
        return website_title


    def website_feed_link(self):
        return self.url
        
    def website_original_link(self):
        response = self.response
        try:
            website_original_link = re.findall('<link>(.*?)<\/link>', response)[0]
        except:
            website_original_link = ''
        return website_original_link

    def last_updated_on(self):
        response = self.response
        try:
            last_updated_on = re.findall('<lastBuildDate>(.*?)</lastBuildDate>')[0]
        except:
            last_updated_on = ''
        return last_updated_on


    def feed_details(self):
        
        items = re.findall(r'<item>[\s\S]*?</item>', self.response)

        data = {}

        for item in items:
            #title of the feed
            try:
                title = re.sub('[\s\S]*<title>','', item)
                title = re.sub(r'<\/title>[\s\S]*','', title, re.DOTALL)
                title = re.sub(r'<!\[CDATA\[','', title, re.DOTALL)
                title = re.sub(r'\]\]>','', title, re.DOTALL)   
            except:
                title= ''
                pass

            #link for the feed
            try:
                feed_link  = re.sub('[\s\S]*<link>','', item)
                feed_link = re.sub(r'<\/link>[\s\S]*','', feed_link, re.DOTALL)
                feed_link = re.sub(r'<!\[CDATA\[','', feed_link, re.DOTALL)
                feed_link = re.sub(r'\]\]>','', feed_link, re.DOTALL)
            except:
                feed_link = ''
                pass

            #published timestamp
            try:
                published_on = re.findall(r'<pubDate>(.*?)</pubDate>', item)[0]
            except:
                published_on = ''
                pass

            #description
            try:
                description = re.sub(r'[\s\S]*<description>','',item)
                description = re.sub(r'<\/description>[\s\S]*','', description, re.DOTALL)
                description = re.sub(r'<!\[CDATA\[','',description, re.DOTALL)
                description = re.sub(r'\]\]>','',description, re.DOTALL)

            except:
                description = ''
                pass

            #all data
            data[title] = [published_on, feed_link, description]
        return data
