from django.contrib import admin

# Register your models here.
from .models import Campaign,Upcoming_Events,Gallery,News,Contact
admin.site.register(Campaign)
admin.site.register(Upcoming_Events)
admin.site.register(Gallery)
admin.site.register(News)
admin.site.register(Contact)
#admin.site.register(About_Us)