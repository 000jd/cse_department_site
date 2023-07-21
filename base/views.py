from django.shortcuts import render

from about.models import Club
from events.models import Notice, Events

# Create your views here.


def homePage(request):
    clubs = Club.objects.all()
    notices = Notice.objects.order_by('-date_added')
    events = Events.objects.order_by('-date_added')
    context = {'clubs': clubs,
               'notices': notices,
               'events': events}
    return render(request, 'screens/home.html', context)

def error_404(request, exception):
    return render(request, '404.html')

def error_500(request):
    return render(request, '500.html')