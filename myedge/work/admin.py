from django.contrib import admin

# Register your models here.
from .models import Campaign,Upcoming_Events,Gallery
admin.site.register(Campaign)
admin.site.register(Upcoming_Events)
admin.site.register(Gallery)
