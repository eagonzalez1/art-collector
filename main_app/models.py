from django.db import models

class Artist(models.Model):
  name = models.CharField(max_length=100)
  about = models.TextField(max_length=500)

  def __str__(self):
    return self.name

class Art(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField('Completion Date')
  description = models.TextField(max_length=500)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
