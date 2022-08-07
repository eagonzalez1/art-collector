from django.db import models
from django.urls import reverse

class Artist(models.Model):
  name = models.CharField(max_length=100)
  about = models.TextField(max_length=1000)
  picture = models.CharField(max_length=250)

  def __str__(self):
    return self.name

class Art(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField('Completion Date')
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  description = models.TextField(max_length=500)
  photo = models.CharField(max_length=250)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('arts_detail', kwargs={'art_id': self.id})
