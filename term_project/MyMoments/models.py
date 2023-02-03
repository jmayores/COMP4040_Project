from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    date    = models.DateField()
    moment  = models.TextField()

    def get_absolute_url_detail(self):
        return reverse('MyMoments-detail', kwargs={'id': self.id})