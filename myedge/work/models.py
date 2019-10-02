from django.db import models
from datetime import date
# Create your models here.

'''class About_Us(models.Model):
    #mission
    mission_title=models.CharField(max_length=100,default=None)
    mission_text=models.TextField(default='')
    #vision
    vision_title=models.CharField(max_length=100,default=None)
    vision_text=models.TextField(default='')
    #history
    history_title=models.CharField(max_length=100,default=None)
    history_text=models.TextField(default='')
'''
class News(models.Model):
    news_title=models.CharField(max_length=100,default=None)
    news_image=models.ImageField(upload_to='media')
    news_text=models.TextField(default='')
   # news_date=models.DateField(blank=True)

class Gallery(models.Model):
    # photo
    gallery_image = models.ImageField(upload_to='media')
    gallery_title = models.CharField(max_length=100,default=None)
    # videos
    # gallery_video=models.
    video_title = models.CharField(max_length=100,default=None)

    # awards
    award_image = models.ImageField(upload_to='media')
    award_title = models.CharField(max_length=200)


class Campaign(models.Model):
    campaign_title = models.CharField(max_length=100,default=None)
    campaign_image=models.ImageField(upload_to='media')
    #campaign_date=models.DateField(blank=True)
    campaign_text=models.TextField(default='')
    campaign_show=models.BooleanField(default='False', null=True)

class Upcoming_Events(models.Model):
    event_images=models.ImageField(upload_to='media')
    event_title=models.CharField(max_length=100,default=None)
    #event_date=models.DateField(default=date.today().strftime('%y-%m-%d'))
    event_venue=models.CharField(max_length=20)

class Contact(models.Model):
    contact_text=models.TextField(default='')
