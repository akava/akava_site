from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'index', name='root'),
    url(r'^(\d+)-([\w_-]+)/$', 'entry', name='blog_entry'),)
