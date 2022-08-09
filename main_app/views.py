from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Art, Photo
import uuid
import boto3


class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def arts_index(request):
  arts = Art.objects.all()
  return render(request, 'arts/index.html', { 'arts': arts })

def arts_detail(request, art_id):
  art = Art.objects.get(id=art_id)
  return render(request, 'arts/detail.html', { 'art': art })

class ArtCreate(CreateView):
  model = Art
  fields = ['title', 'description']

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class ArtUpdate(UpdateView):
  model = Art
  fields = ['title', 'description']

class ArtDelete(DeleteView):
  model = Art
  success_url = '/Arts/'



S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'marich-art-collecotr-app'

def add_photo(request, art_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
		# uuid.uuid4().hex generates a random hexadecimal Universally Unique Identifier
    # Add on the file extension using photo_file.name[photo_file.name.rfind('.'):]
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to art_id or art (if you have a art object)
      photo = Photo(url=url, art_id=art_id)
      # Remove old photo if it exists
      art_photo = Photo.objects.filter(art_id=art_id)
      if art_photo.first():
        art_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('arts_detail', art_id=art_id)