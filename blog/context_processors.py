from blog.models import Entry


def featured_entries(request):
    entries = Entry.objects.all() if request.user.is_superuser else Entry.live.all()
    featured = entries.filter(featured__exact=True).all()
    return {'featured_entries': featured}