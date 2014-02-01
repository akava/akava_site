from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from settings import FEED_BURNER_URL
from blog.feeds import LatestEntriesFeed

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='home'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^about_me/', 'blog.views.about_me', name='about_me'),

    # feed
    url(r'^feed/$', RedirectView.as_view(url=FEED_BURNER_URL, permanent=True), name='feed'),
    url(r'^feed_for_burner/$', LatestEntriesFeed(), name='feed_for_burner'),

    # request proxies
    url(r'^request_proxy/([\w_-]+)/$', 'request_proxy.views.call_proxy', name='call_proxy'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
