from django.db import models
from datetime import datetime


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=400)
    finished = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now,blank=True)
    image = models.CharField(max_length=400,default = "https://images.unsplash.com/photo-1471107340929-a87cd0f5b5f3?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=966&q=80")

    def __str__(self):
        return  self.title
