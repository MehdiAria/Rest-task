from django.contrib import admin

from .models import *


class RateShow(admin.ModelAdmin):
    """
    An admin model class for costuming rate on admin panel.
    """
    list_display = ['user', 'rate', 'post']
    search_fields = ['user']
    list_per_page = 10


class PostShow(admin.ModelAdmin):
    """
    An admin model class for posts categories on admin panel.
    """
    list_display = ['title']
    search_fields = ['title']
    list_per_page = 10


# register the models
admin.site.register(Post, PostShow)
admin.site.register(Rate, RateShow)
