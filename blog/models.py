import datetime
from django.db import models

class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = ((LIVE_STATUS, 'Live'),
                      (DRAFT_STATUS, 'Draft'),
                      (HIDDEN_STATUS, "Hidden"))

    title = models.CharField(max_length=250)
    slug = models.SlugField(help_text=u'Used in the URL of the entry.')
    published = models.DateTimeField(default=datetime.datetime.today)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS,
        help_text=u'Only entries with "Live" status will be displayed '\
                  u'publicly.')
    text_markdown = models.TextField(help_text=u'Use Markdown syntax',
                                    blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Entries'

    def __unicode__(self):
        return self.title

