from django.contrib.syndication.views import Feed
from models import Entry


class LatestEntriesFeed(Feed):
    title = "Andrei Kavaleu's blog"
    link = "/blog/"

    def items(self):
        return list(Entry.objects.filter(status__exact=Entry.LIVE_STATUS).all()[:10])

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text
