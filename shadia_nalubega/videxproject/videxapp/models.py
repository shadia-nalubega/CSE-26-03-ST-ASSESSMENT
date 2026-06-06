from django.db import models


class Video(models.Model):
    QUALITY_CHOICES = [
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
        ('4K', '4K'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    quality = models.CharField(max_length=10, choices=QUALITY_CHOICES)
    date_of_publishing = models.DateField()
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title