from django.db import models
from django.utils.text import slugify
import uuid

class Gallery(models.Model):
    """
    Model representing a gallery.
    """
    topic = models.CharField(max_length=255, db_index=True)  
    slug = models.SlugField(blank=True, null=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='upload/', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        """
        Returns a string representation of the gallery.
        """
        return self.topic
    
    def save(self, *args, **kwargs):
        """
        Overrides the default save method to generate a slug based on the topic field.
        """
        if not self.slug:
            self.slug = slugify(self.topic)
        
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Returns the absolute URL of the gallery.
        """
        return f'/{self.slug}/'
    
    def get_image(self):
        """
        Returns the URL of the image associated with the gallery.
        """
        if self.image:
            return 'http://127.0.0.1:8000/' + self.image.url
        return ''

class Club(models.Model):
    """
    Model representing a club.
    """
    name = models.CharField(max_length=100, db_index=True)  
    slug = models.SlugField(blank=True, null=True, db_index=True)
    description = models.TextField()
    image = models.ImageField(upload_to='club_images/')
    url = models.URLField()

    def __str__(self):
        """
        Returns a string representation of the club.
        """
        return self.name
    
    def save(self, *args, **kwargs):
        """
        Overrides the default save method to generate a slug based on the name field.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        
        super().save(*args, **kwargs)

class Message(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
class Resources(models.Model):
    """
    Model representing resources with topics, description, image, and URL link.
    """
    topic = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='resources/', blank=True)
    url_link = models.URLField()

    def __str__(self):
        """
        Returns a string representation of the resource.
        """
        return self.topic

