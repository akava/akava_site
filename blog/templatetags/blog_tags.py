from django import template
from blog.models import Entry

register = template.Library()


@register.tag()
def load_featured_entries(parser, token):
    """
    Adds featured posts to context with provided name

    Example:

        {{% load_featured_entries as featured %}}
    """
    args = token.split_contents()
    if len(args) != 3 and args[1] != 'as':
        raise template.TemplateSyntaxError("%s tag tags exactly 3 arguments. The second one of them is 'as'" % args[0])

    return LoadFeaturedEntriesNode(args[2])


class LoadFeaturedEntriesNode(template.Node):
    def __init__(self, target):
        self.target = target

    def render(self, context):
        featured = Entry.live.filter(featured__exact=True).all()
        context[self.target] = featured

        return ""
