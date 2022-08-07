from django.shortcuts import render
from django.http import HttpResponse



def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')


def arts_index(request):
  return render(request, 'arts/index.html', { 'arts': arts })