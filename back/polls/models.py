from django.db import models
from django.conf import settings

# Create your models here.
class Poll(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre = models.ManyToManyField('movies.Genre', related_name='polls')


