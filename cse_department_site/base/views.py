from django.shortcuts import render

from about.models import Club
from events.models import Notice, Events

from django.core.cache import cache

def homePage(request):
    data_payload = cache.get('home_page_data')

    if not data_payload:
        clubs = Club.objects.all()
        notices = Notice.objects.order_by('-date_added')
        events = Events.objects.order_by('-date_added')
        context = {'clubs': clubs, 'notices': notices, 'events': events}
        # Cache the data_payload for 15 minutes (900 seconds)
        cache.set('home_page_data', context, 900)
    else:
        context = data_payload

    return render(request, 'screens/home.html', context)

def error_404(request, exception):
    return render(request, '404.html')

def error_500(request):
    return render(request, '500.html')
