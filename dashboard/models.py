from django.db import models
from django.utils import timezone
# Create your models here.

class Meme(models.Model):
    name = models.CharField(max_length=20, blank=False)
    caption = models.CharField(max_length=200, blank=False)
    url = models.URLField(max_length=200, blank=False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
