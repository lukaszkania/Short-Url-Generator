from django.contrib import admin
from .models import Url

# Register your models here.

class UrlAdmin(admin.ModelAdmin):
    list_display = ('pk', 'url', 'shorted_url')

admin.site.register(Url, UrlAdmin)