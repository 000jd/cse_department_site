from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    """
    Custom user model.
    """
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('faculty', 'faculty Member'),
        ('faculty', 'Staff Member'),
        ('alumni', 'Alumni'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Student(models.Model):
    """
    Model representing a student.
    """
    YEAR_TYPE_CHOICES = (
        ('First Year', 'First Year'),
        ('Second Year', 'Second Year'),
        ('Third Year', 'Third Year'),
        ('Final Year', 'Final Year'),
    )

    SEMESTER_TYPE_CHOICES = (
        ('Semester 1', 'Semester 1'),
        ('Semester 2', 'Semester 2'),
        ('Semester 3', 'Semester 3'),
        ('Semester 4', 'Semester 4'),
        ('Semester 5', 'Semester 5'),
        ('Semester 6', 'Semester 6'),
        ('Semester 7', 'Semester 7'),
        ('Semester 8', 'Semester 8'),
    )
    
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='Student')
    student_id = models.CharField(max_length=100, default="As per colage records")
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='students/', blank=True)
    contact_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    year = models.CharField(max_length=100, choices=YEAR_TYPE_CHOICES)
    semester = models.CharField(max_length=100, choices=SEMESTER_TYPE_CHOICES)  # Provide a default value
    field_of_interest = models.CharField(max_length=100, blank=True, default="web dev / devops")

    def __str__(self):
        """
        Returns a string representation of the student.
        """
        return self.full_name


class Alumni(models.Model):
    """
    Model representing an alumni.
    """
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='alumni')
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='alumnis/', blank=True)
    collage_id =  models.CharField(max_length=100, default="As per colage records")
    Degree =  models.CharField(max_length=100, default = "B.Tech (CSE)")
    Batch =  models.CharField(max_length=100, default="2019-2022")
    contact_number = models.IntegerField()
    current_company = models.CharField(max_length=100, default="If any else None")
    graduation_year = models.IntegerField(default="022")
    email = models.EmailField(max_length=254)

    def __str__(self):
        """
        Returns a string representation of the alumni.
        """
        return self.full_name


class Staff(models.Model):
    """
    Model representing a staff member.
    """
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='staff')
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='staffs/', blank=True)
    designation = models.CharField(max_length=100, default="Assistant Professor")
    contact_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=254, default='Null')
    qualification = models.CharField(max_length=100, blank=True)
    experience = models.CharField(max_length=100, blank=True)

    def __str__(self):
        """
        Returns a string representation of the staff member.
        """
        return self.full_name
