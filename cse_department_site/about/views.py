from django.shortcuts import render
from .models import Club, Gallery
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


def student(request):
    data = Student.objects.all()
    context = {"students": data}
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



def About(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()

    messages.success(request, "massge sent success fully..")

    context = {'form': form}
    return render(request, 'screens/About.html', context)

def alumai(request):
    data = Alumni.objects.all()
    context = {"alumais": data}
    return render(request, 'screens/alumai.html', context)

def resources(request):
    #data = Alumni.objects.all()
    #context = {"resources": data}
    return render(request, 'screens/resources.html'#, context
                  )
