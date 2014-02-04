from django.http import HttpResponse, Http404
from settings import SMS_SECRET

from calendar_sms import sms


def send(request):
    secret = request.GET.get('secret')
    text = request.GET.get('text')
    if not secret or secret != SMS_SECRET or not text:
        raise Http404

    return HttpResponse(sms.sendSMS(text))