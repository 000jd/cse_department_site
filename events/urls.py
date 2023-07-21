from django.urls import path
from . import views

urlpatterns = [
    path('notice-and-events/', views.notice_and_events, name='notice_and_events'),
]