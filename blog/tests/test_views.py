import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from blog.models import Entry


class IndexPageTests(TestCase):
    def setUp(self):
        self.entries = create_entries()

    def test_user_sees_only_live_items(self):
        response_content = self.client.get('/').content

        self.assertIn(self.entries.live1.title, response_content)
        self.assertIn(self.entries.live2.title, response_content)
        self.assertNotIn(self.entries.draft.title, response_content)
        self.assertNotIn(self.entries.hidden.title, response_content)

    def test_output_html_has_links_to_individual_entries(self):
        response_content = self.client.get('/').content

        self.assertIn(self.entries.live1.get_absolute_url(), response_content)
        self.assertIn(self.entries.live2.get_absolute_url(), response_content)

    def test_entries_sorted_by_publish_date(self):
        self.entries.live1.published = timezone.now() - datetime.timedelta(days=5)
        self.entries.live1.save()
        self.entries.live2.published = timezone.now() + datetime.timedelta(days=5)
        self.entries.live2.save()
        self.entries.live3.published = timezone.now()
        self.entries.live3.save()

        page_entries = self.client.get("/").context['entries']

        # order should be 2-3-1
        self.assertEqual(list(page_entries), list([self.entries.live2, self.entries.live3, self.entries.live1]))

    def test_featured_entries_are_shown_on_featured_section(self):
        self.entries.live2.featured = True
        self.entries.live2.save()
        self.entries.live3.featured = True
        self.entries.live3.save()

        featured_entries = self.client.get("/").context['featured_entries']

        self.assertEqual(list(featured_entries),
                         list([self.entries.live2, self.entries.live3]))


class AdminTests(TestCase):
    def setUp(self):
        self.entries = create_entries()

        self.admin = User.objects.create_superuser('admin', 'admin@site.com', password='secret')
        self.admin.save()
        self.client.login(username='admin', password='secret')

    def test_admin_sees_all_entries(self):
        response_content = (self.client.get('/')).content

        # output html has only live entries
        self.assertIn(self.entries.live1.title, response_content)
        self.assertIn(self.entries.live2.title, response_content)
        self.assertIn(self.entries.draft.title, response_content)
        self.assertIn(self.entries.hidden.title, response_content)


class EntryPageTests(TestCase):
    def setUp(self):
        self.entry = create_entries().live1

    def test_entry_can_be_retrieved_by_its_url(self):
        self.entry.text = 'django is the capital of Pythonia'
        self.entry.save()

        response = self.client.get(self.entry.get_absolute_url())

        self.assertEqual(response.context['entry'], self.entry)
        self.assertIn(self.entry.title, response.content)
        self.assertIn(self.entry.text, response.content)

    def test_404_is_returned_for_non_existing_entries(self):
        non_valid_url = reverse('blog:blog_entry', args=[999, 'slug-slug'])
        response = self.client.get(non_valid_url)
        self.assertEqual(response.status_code, 404)

    def test_client_is_redirected_if_slug_doesnt_match(self):
        non_valid_url = reverse('blog:blog_entry', args=[self.entry.id, 'slug-slug'])
        response = self.client.get(non_valid_url)

        self.assertRedirects(response, self.entry.get_absolute_url())


#factories
def create_entries():
    class Entries():
        live1 = None
        live2 = None
        live3 = None
        draft = None
        hidden = None

    entries = Entries()
    entries.live1 = Entry(title='Usage of context processors in Django', slug='context-processor',
                                status=Entry.LIVE_STATUS)
    entries.live1.save()
    entries.live2 = Entry(title='Tz aware datetime vs naive datetime', slug='tz-aware',
                                status=Entry.LIVE_STATUS)
    entries.live2.save()
    entries.live3 = Entry(title='Attribute accessible dictionary', slug='attr-dict',
                                status=Entry.LIVE_STATUS)
    entries.live3.save()
    entries.draft = Entry(title='Draft entry', slug='draft', status=Entry.DRAFT_STATUS)
    entries.draft.save()
    entries.hidden = Entry(title='Hidden entry', slug='hidden', status=Entry.HIDDEN_STATUS)
    entries.hidden.save()

    return entries
