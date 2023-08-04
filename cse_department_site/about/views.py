from django.shortcuts import render
from .models import Gallery, Resources
from .forms import MessageForm
from django.contrib import messages
from accounts.models import Student, Staff, Alumni

from django.core.cache import cache

def carousel_images(request):
    data_payload = cache.get('carousel_images_data')

    if not data_payload:
        data = Gallery.objects.all()[:6]
        context = {'images': data}
        # Cache the data_payload for 1 hour (3600 seconds)
        cache.set('carousel_images_data', context, 3600)
    else:
        context = data_payload

    return render(request, 'components/carousel.html', context)


def gallery_images(request):
    data_payload = cache.get('gallery_images_data')

    if not data_payload:
        images = Gallery.objects.all()
        context = {'images': images}
        # Cache the data_payload for 1 hour (3600 seconds)
        cache.set('gallery_images_data', context, 3600)
    else:
        context = data_payload

    return render(request, 'screens/gallery.html', context)

def About(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()

    messages.success(request, "message sent successfully..")

    context = {'form': form}
    return render(request, 'screens/About.html', context)


def student(request):
    data_payload = cache.get('students_list_data')

    if not data_payload:
        data = Student.objects.all()
        students_list = []
        for student in data:
            students_info = {
                'student_id': student.student_id,
                "full_name": student.full_name,
                "email": student.email,
                "image": student.image.url if student.image else None,
                'year': student.year,
                'semester': student.semester,
            }
            students_list.append(students_info)
        context = {"students_list": students_list}
        # Cache the data_payload for 1 hour (3600 seconds)
        cache.set('students_list_data', context, 3600)
    else:
        context = data_payload

    return render(request, 'screens/student.html', context)


def faculty(request):
    data_payload = cache.get('faculty_list_data')

    if not data_payload:
        data = Staff.objects.all()
        faculty_list = []
        for faculty in data:
            faculty_info = {
                "full_name": faculty.full_name,
                "qualification": faculty.qualification,
                "email": faculty.email,
                "image": faculty.image.url if faculty.image else None,
            }
            faculty_list.append(faculty_info)
        context = {"faculty_list": faculty_list}
        # Cache the data_payload for 1 hour (3600 seconds)
        cache.set('faculty_list_data', context, 3600)
    else:
        context = data_payload

    return render(request, 'screens/faculty.html', context)

def alumai(request):
    data_payload = cache.get('alumais_list_data')

    if not data_payload:
        data = Alumni.objects.all()
        alumais_list = []
        for alumai in data:
            alumais_info = {
                "full_name": alumai.full_name,
                "graduation_year": alumai.graduation_year,
                "current_company": alumai.current_company,
                "email": alumai.email,
                "image": alumai.image.url if alumai.image else None,
            }
            alumais_list.append(alumais_info)
        context = {"alumais_list": alumais_list}
        # Cache the data_payload for 1 hour (3600 seconds)
        cache.set('alumais_list_data', context, 3600)
    else:
        context = data_payload

    return render(request, 'screens/alumai.html', context)

def resources(request):
    data_payload = cache.get('resources_data')

    if not data_payload:
        data = Resources.objects.all()
        context = {"resources": data}
        # Cache the data_payload for 1 hour (3600 seconds)
        cache.set('resources_data', context, 3600)
    else:
        context = data_payload

    return render(request, 'screens/resources.html', context)