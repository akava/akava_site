from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from blog.models import Entry


def index(request):
    entries = Entry.objects.all() if request.user.is_superuser else Entry.live.all()
    return render(request,
                  'blog/index.html',
                  {'entries': entries})


def entry(request, id, slug):
    entries = Entry.objects if request.user.is_superuser else Entry.live
    try:
        entry = entries.get(id=id)
    except Entry.DoesNotExist:
        raise Http404

    if slug != entry.slug:
        return HttpResponseRedirect(entry.get_absolute_url())
    return render(request,
                  'blog/entry.html',
                  {'item': entry})
