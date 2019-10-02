from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from .models import Campaign,Upcoming_Events,News,Contact
# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"
    def get(self,request):
        obj=Campaign.objects.all()
        args={'obj':obj}
        return render(request,'index.html',args)
        
class AboutPageView(TemplateView):
    template_name = "about.html"
class AwardsPageView(TemplateView):
    template_name = "awards.html"

class CampaignsPageView(TemplateView):
    template_name = "campaigns.html" 
    def get(self,request):
        obj=Campaign.objects.all()
        print(">>>>>>>>>>>>>>>>>>>",obj[0].campaign_title)
        title = map(lambda o:o.campaign_title, obj)
        # title =['dog', 'cat','horse']
        args={'obj':obj,'title':title}
        return render(request,"campaigns.html" ,args)


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
