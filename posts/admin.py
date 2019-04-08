from django.contrib import admin
from .models import Post

# register the Post class from the models.py to access admin section of django
admin.site.register(Post)