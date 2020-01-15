from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    text = models.TextField(max_length=256)
    date = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ["-date"]

    def publish(self):
        self.date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.text

