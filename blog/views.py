from django.shortcuts import render
from blog.models import Entry

def index(request):
    entries = Entry.objects.filter(status__exact=Entry.LIVE_STATUS)

    return render(request,
                  'blog/index.html',
                  {'entries': entries})
