from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
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
    form.instance.user = self.request.user
    return super().form_valid(form)

class ArtUpdate(LoginRequiredMixin, UpdateView):
  model = Art
  fields = ['title', 'description']

class ArtDelete(LoginRequiredMixin, DeleteView):
  model = Art
  success_url = '/arts/'


S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'marich-art-collecotr-app'

def add_photo(request, art_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, art_id=art_id)
      art_photo = Photo.objects.filter(art_id=art_id)
      if art_photo.first():
        art_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('arts_detail', art_id=art_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('arts_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
