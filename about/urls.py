from django.urls import path
from . import views

urlpatterns = [
    path('gallery', views.gallery_images, name = 'gallery'),
    path('student', views.student, name = 'student'),
    path('facalty', views.student, name = 'facalty'),
]