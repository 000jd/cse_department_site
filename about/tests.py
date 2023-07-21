from django.test import TestCase
from .models import Gallery, Club

class GalleryTestCase(TestCase):
    def setUp(self):
        # Create a test gallery
        self.gallery = Gallery.objects.create(
            topic='Test Gallery',
            slug='test-gallery',
            description='Test gallery description',
            image='path/to/test-image.jpg'
        )

    def test_gallery_creation(self):
        # Check if the gallery is created correctly
        self.assertEqual(self.gallery.topic, 'Test Gallery')
        self.assertEqual(self.gallery.slug, 'test-gallery')
        self.assertEqual(self.gallery.description, 'Test gallery description')
        self.assertEqual(self.gallery.image, 'path/to/test-image.jpg')

    def test_get_absolute_url(self):
        # Test the get_absolute_url method
        expected_url = '/test-gallery/'
        self.assertEqual(self.gallery.get_absolute_url(), expected_url)

    def test_get_image(self):
        # Test the get_image method
        expected_image_url = 'http://127.0.0.1:5500/path/to/test-image.jpg'
        self.assertEqual(self.gallery.get_image(), expected_image_url)

class ClubTestCase(TestCase):
    def setUp(self):
        # Create a test club
        self.club = Club.objects.create(
            name='Test Club',
            slug='test-club',
            description='Test club description',
            image='path/to/test-image.jpg',
            url='http://example.com'
        )

    def test_club_creation(self):
        # Check if the club is created correctly
        self.assertEqual(self.club.name, 'Test Club')
        self.assertEqual(self.club.slug, 'test-club')
        self.assertEqual(self.club.description, 'Test club description')
        self.assertEqual(self.club.image, 'path/to/test-image.jpg')
        self.assertEqual(self.club.url, 'http://example.com')

    def test_save_method(self):
        # Test the save method to generate a slug
        self.assertEqual(self.club.slug, 'test-club')

        # Update the club name
        self.club.name = 'Updated Club'
        self.club.save()
        self.assertEqual(self.club.slug, 'updated-club')