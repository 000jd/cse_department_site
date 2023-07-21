from django.shortcuts import render
from .models import Notice, Events

def notice_and_events(request):
    """
    Retrieves all notices and events, ordered by date added (latest first).
    Renders the 'notice_and_events.html' template with the retrieved data.
    """
    notices = Notice.objects.order_by('-date_added')
    events = Events.objects.order_by('-date_added')
    context = {
        'notices': notices,
        'events': events
    }
    return render(request, 'components/notice_and_events.html', context)
