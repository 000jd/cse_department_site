from django.shortcuts import render
from .models import Notice, Events

def notice_and_events(request):
    notices = Notice.objects.order_by('-date_added')
    events = Events.objects.order_by('-date_added')
    context = {
        'notices': notices,
        'events': events
    }
    return render(request, 'components/notice_and_events.html', context)
