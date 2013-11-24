from django.conf.urls import patterns, include, url
from blog.feeds import LatestEntriesFeed


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='home'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^about_me/', 'blog.views.about_me', name='about_me'),

    # feed
    url(r'^feed/$', LatestEntriesFeed(), name='feed'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
