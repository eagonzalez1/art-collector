from django.contrib import admin
# import your models here
from .models import Art, Artist, Photo

# Register your models here
admin.site.register(Art)
admin.site.register(Artist)
admin.site.register(Photo)