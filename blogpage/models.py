from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    image=models.FileField(upload_to="blogimag/",max_length=250,null=True,default=None)
   
    def __str__(self):
        return self.title
