from django.shortcuts import render



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def arts_index(request):
  return render(request, 'arts/index.html', { 'arts': arts })