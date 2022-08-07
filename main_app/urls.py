from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('arts/', views.arts_index, name='arts_index'),
  path('arts/<int:art_id>/', views.arts_detail, name='arts_detail'),
  path('arts/create/', views.ArtCreate.as_view(), name='arts_create'),

]