from django.conf.urls import url
from work import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^awards/$', views.AwardsPageView.as_view(), name='awards'),
    url(r'^campaigns/$', views.CampaignsPageView.as_view(), name='campaign'),
    url(r'^contact/$', views.ContactPageView.as_view(), name='contact'),
    url(r'^gallary/$', views.GallaryPageView.as_view(), name='gallary'),
    url(r'^history/$', views.HistoryPageView.as_view(), name='history'),
    url(r'^mission/$', views.MissionPageView.as_view(), name='mission'),
    url(r'^news/$', views.NewsPageView.as_view(), name='news'),
    url(r'^videos/$', views.VideosPageView.as_view(), name='videos'),
    url(r'^vision/$', views.VisionPageView.as_view(), name='vision'),
]