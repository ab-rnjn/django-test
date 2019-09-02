from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from .models import Campaign, Upcoming_Events, Gallery
# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"
    def __index__(request):
        obj=Campaign.objects.all()
        return render(request,'../../../index.html',{'obj':obj})
        
class AboutPageView(TemplateView):
    template_name = "about.html"
class AwardsPageView(TemplateView):
    template_name = "awards.html"

class CampaignsPageView(TemplateView):
    template_name = "campaigns.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class GallaryPageView(TemplateView):
    template_name = "gallary.html"

class HistoryPageView(TemplateView):
    template_name = "history.html"

class MissionPageView(TemplateView):
    template_name = "mission.html"

class NewsPageView(TemplateView):
    template_name = "news.html"

class VideosPageView(TemplateView):
    template_name = "videos.html"

class VisionPageView(TemplateView):
    template_name = "vision.html"
