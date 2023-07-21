from django.shortcuts import render
from .models import Gallery, Resources
from .forms import MessageForm
from django.contrib import messages
from accounts.models import Student, Staff, Alumni


def carousel_images(request):
    """
    Retrieves the latest 6 gallery images for the carousel.
    Renders the 'carousel.html' template with the retrieved images.
    """
    data = Gallery.objects.all()[:6]
    context = {'images': data}
    return render(request, 'components/carousel.html', context)


def gallery_images(request):
    """
    Retrieves all gallery images.
    Renders the 'gallery.html' template with the retrieved images.
    """
    images = Gallery.objects.all()
    context = {'images': images}
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
    return render(request, 'screens/student.html', context)


def faculty(request):
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
    return render(request, 'screens/faculty.html', context)

def alumai(request):
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
    return render(request, 'screens/alumai.html', context)

def resources(request):
    data = Resources.objects.all()
    context = {"resources": data}
    return render(request, 'screens/resources.html', context)
