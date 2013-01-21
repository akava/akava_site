from django.contrib import admin

from models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'status', 'created', 'edited', 'published']
    prepopulated_fields = {'slug': ['title']}


admin.site.register(Entry, EntryAdmin)

