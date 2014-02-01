from django.http.response import Http404, HttpResponse
from request_proxy.models import Proxy

import requests


def call_proxy(request, slug):
    proxies = Proxy.objects
    try:
        proxy = proxies.get(slug=slug)
    except Proxy.DoesNotExist:
        raise Http404

    url = proxy.url + "&" + request.GET.urlencode()

    r = requests.get(url)

    return HttpResponse(r.text)
