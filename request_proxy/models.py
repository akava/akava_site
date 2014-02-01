from django.core.urlresolvers import reverse
from django.db import models


class Proxy(models.Model):
    GET = 'GET'
    POST = 'POST'
    METHODS = ((GET, 'GET'),
               (POST, 'POST'),)

    name = models.CharField(max_length=100)
    slug = models.SlugField(help_text=u'Used in the URL of the proxy.')
    url = models.URLField()
    #method = models.CharField(choices=METHODS, default=GET, max_length=10)
    #body = models.TextField(blank=True, null=True)
    # last_call
    # last call status

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Proxies'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('call_proxy', args=[self.slug])