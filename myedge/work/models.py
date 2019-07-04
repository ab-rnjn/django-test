from django.db import models

# Create your models here.
class Campaign(models.Model):
    campaign_image=models.ImageField()
    campaign_title=models.CharField(max_length=100)
    campaign_text=models.TextField()

class Upcoming_Events(models.Model):
    event_images=models.ImageField()
    event_title=models.CharField(max_length=100)
    event_date=models.DateField()
    event_venue=models.CharField(max_length=20)

class Gallery(models.Model):
    gallery_image=models.ImageField()
