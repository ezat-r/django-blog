from django.db import models
from django.utils import timezone

class Post(models.Model):
    ### A single Blog post

    # blog properties  
    title = models.CharField(max_length=200)
    content = models.TextField()
    createdDate = models.TimeField(auto_now_add=True)
    publishedDate = models.TimeField(blank=True, null=True, default=timezone.now())
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    # image element with the 'upload_to' property referencing the 'img' folder in the 'media' folder
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __unicode__(self):
        return self.title