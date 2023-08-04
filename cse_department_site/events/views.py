from django.shortcuts import render
from .models import Notice, Events

from django.core.cache import cache

def notice_and_events(request):
    data_payload = cache.get('notice_and_events_data')
    
    if not data_payload:
        notices = Notice.objects.order_by('-date_added')
        events = Events.objects.order_by('-date_added')
        context = {
            'notices': notices,
            'events': events
        }
        # Cache the data_payload for 15 minutes (900 seconds)
        cache.set('notice_and_events_data', context, 900)
    else:
        context = data_payload

    return render(request, 'components/notice_and_events.html', context)