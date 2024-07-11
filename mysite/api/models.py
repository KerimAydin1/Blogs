from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Users(models.Model):
    username = models.CharField(max_length=8)
    password = models.CharField(max_length=8)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
