from django.contrib import admin

from aaa.models import *


class AdsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_published']
    list_display_links = ['name']
    search_fields = ['name']

admin.site.register(Ads, AdsAdmin)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Location)
