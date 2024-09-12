from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  university_name = models.CharField(max_length=200)
  department = models.CharField(max_length=50)
  batch = models.CharField(max_length=50)
  roll = models.IntegerField()
  address = models.CharField(max_length=100)
  student_img = models.ImageField(upload_to='student/')

  def __str__(self):
    return self.name
  
class Gallery(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  gallery_img = models.ImageField(upload_to='gallery/')

from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    excerpt = models.TextField()
    image = models.ImageField(upload_to='blog/')
    published_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class NumberArray(models.Model):
    name = models.CharField(max_length=100)  # Optional field to identify the array
    data = models.JSONField()  # Stores the array of numbers

    def __str__(self):
        return self.name
    
from django.db import models

class Model(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='model_images/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
