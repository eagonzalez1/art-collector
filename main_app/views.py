from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Art, Artist


def home(request):
  return render(request, 'home.html')

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
  fields = '__all__'
  success_url = '/arts/'

class ArtUpdate(UpdateView):
  model = Art
  fields = ['title', 'date', 'artist', 'description']

class ArtDelete(DeleteView):
  model = Art
  success_url = '/Arts/'