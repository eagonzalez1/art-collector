from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Artist(models.Model):
  name = models.CharField(max_length=100)
  contact = models.CharField(max_length=100)
  about = models.TextField(max_length=1000)

  def __str__(self):
    return self.name

class Art(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField('Completion Date')
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  description = models.TextField(max_length=500)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('arts_detail', kwargs={'art_id': self.id})

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=250)
  art = models.OneToOneField(Art, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for art_id: {self.art_id} @{self.url}"
