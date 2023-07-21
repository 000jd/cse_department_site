from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import AlumniForm, CreateUserForm, StaffForm, StudentForm
from django.contrib import messages


def register_page(request):
    """
    Renders the registration page and handles user registration.
    If the user is already authenticated, redirects to the home page.
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                user_type = form.cleaned_data.get('user_type')
                if user_type == 'student':
                    return redirect('register_student')
                elif user_type == 'alumni':
                    return redirect('register_alumni')
                elif user_type == 'staff':
                    return redirect('register_staff')

        return render(request, 'components/register.html', context={'form': form})


@login_required
def student_form(request):
    """
    Renders the student registration form and handles form submission.
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('home')
    else:
        form = StudentForm()

    return render(request, 'components/student_form.html', context={'form': form})


@login_required
def alumni_form(request):
    """
    Renders the alumni registration form and handles form submission.
    """
    if request.method == 'POST':
        form = AlumniForm(request.POST)
        if form.is_valid():
            alumni = form.save(commit=False)
            alumni.user = request.user
            alumni.save()
            return redirect('home')
    else:
        form = AlumniForm()

    return render(request, 'components/alumni_form.html', context={'form': form})


@login_required
def staff_form(request):
    """
    Renders the staff registration form and handles form submission.
    """
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.user = request.user
            staff.save()
            return redirect('home')
    else:
        form = StaffForm()

    return render(request, 'components/staff_form.html', context={'form': form})


def login_page(request):
    """
    Renders the login page and handles user authentication.
    If the user is already authenticated, redirects to the home page.
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, 'components/login.html')


@login_required
def logout_user(request):
    """
    Logs out the current user and redirects them to the login page.
    """
    logout(request)
    messages.info(request, "You have been successfully logged out.")
    return redirect('home')
