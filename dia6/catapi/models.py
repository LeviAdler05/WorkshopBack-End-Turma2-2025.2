from django.db import models

class CatImage(models.Model):
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_url

class CatImageError(models.Model):
    error_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.error_message[:50] + "..."