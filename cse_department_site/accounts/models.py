from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    """
    Custom user model.
    """
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('staff', 'Staff Member'),
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
        ('first', 'First Year'),
        ('second', 'Second Year'),
        ('third', 'Third Year'),
        ('final', 'Final Year'),
    )

    SEMESTER_TYPE_CHOICES = (
        ('sem1', 'Semester 1'),
        ('sem2', 'Semester 2'),
        ('sem3', 'Semester 3'),
        ('sem4', 'Semester 4'),
        ('sem5', 'Semester 5'),
        ('sem6', 'Semester 6'),
        ('sem7', 'Semester 7'),
        ('sem8', 'Semester 8'),
    )
    
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='Student')
    student_id = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='students/', blank=True)
    contact_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    year = models.CharField(max_length=100, choices=YEAR_TYPE_CHOICES)
    semester = models.CharField(max_length=100, choices=SEMESTER_TYPE_CHOICES)  # Provide a default value
    field_of_interest = models.CharField(max_length=100, blank=True)

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
    contact_number = models.IntegerField()
    current_company = models.CharField(max_length=100)
    graduation_year = models.IntegerField()
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
    designation = models.CharField(max_length=100)
    contact_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=254, default='Null')
    qualification = models.CharField(max_length=100, blank=True, default='Null')
    experience = models.CharField(max_length=100, blank=True, default='Null')

    def __str__(self):
        """
        Returns a string representation of the staff member.
        """
        return self.full_name
