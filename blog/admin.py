from django.contrib import admin
from .models import Post #register post model

#add post model to admin
admin.site.register(Post)
