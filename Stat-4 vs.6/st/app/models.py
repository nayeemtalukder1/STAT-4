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
  phone = models.CharField(default="01",max_length=100)
  student_img = models.ImageField(upload_to='student/')

  def __str__(self):
    return self.name
  

#Post 

# myapp/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('pending', 'Pending')
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    excerpt = models.TextField()
    image = models.ImageField(upload_to='blog/')
    published_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
#gallery

class Gallery(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gallery_img = models.ImageField(upload_to='gallery/')
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='P',
    )

    def __str__(self):
        return f"{self.user.username} - {self.get_status_display()}"

#pdf
# models.py

class PDFDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    pending = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.title} - {'Pending' if self.pending else 'Approved'}"

    
#model 1
class NumberArray(models.Model):
    name = models.CharField(max_length=100)
    data = models.JSONField()  # Stores the array of numbers

    def __str__(self):
        return self.name
    

