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
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='alumni')
    student_id = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    year = models.IntegerField()
    


    def __str__(self):
        """
        Returns a string representation of the student.
        """
        return self.full_name


class Alumni(models.Model):
    """
    Model representing an alumni.
    """
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='student')
    full_name = models.CharField(max_length=100)
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
    contact_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns a string representation of the staff member.
        """
        return self.full_name
