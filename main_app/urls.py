from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('arts/', views.arts_index, name='arts_index'),
  path('arts/<int:art_id>/', views.arts_detail, name='arts_detail'),
  path('arts/create/', views.ArtCreate.as_view(), name='arts_create'),
  path('arts/<int:pk>/update/', views.ArtUpdate.as_view(), name='arts_update'),
  path('arts/<int:pk>/delete/', views.ArtDelete.as_view(), name='arts_delete'),
  path('arts/<int:art_id>/add_photo/', views.add_photo, name='add_photo'),
]