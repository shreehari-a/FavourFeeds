from django_cron import CronJobBase, Schedule
from rss.models import FeedWebsite, User_FeedWebsite, FeedDetail
import feedly
# from rss.views import feed_id_identifier
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        # pass    # do your thing here
        obj = FeedWebsite.objects.filter()
        for item in obj:
        	data = feedly.feed_parser(str(item.website_feed_url))

      #   	website_title = data.website_title()
    		# website_feed_url = data.website_feed_link()
    		# website_url = data.website_original_link()
    		last_updated_on = data.last_updated_on()
    		feed_details = data.feed_details()

        	web_obj = FeedWebsite()
        	
        	if last_updated_on:
        		web_obj.last_updated_on = last_updated_on
        	# for this url find feed_id and update the shit

        	web_obj.update()

        	#
        	
