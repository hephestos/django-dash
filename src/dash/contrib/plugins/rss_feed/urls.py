from django.conf.urls import patterns, url

from . import views

urlpatterns = [ 
    url(r'^get_feed/(?P<layout_uid>[\w_]+)/(?P<placeholder_uid>[\w_]+)/(?P<plugin_uid>[\w_\-]+)/$', \
        views.get_feed, name='dash.contrib.plugins.rss_feed.get_feed'),
]
