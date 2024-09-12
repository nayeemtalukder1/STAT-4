from django.contrib import admin
from . models import Student,Gallery,BlogPost,Model
# Register your models here.


admin.site.register(BlogPost)
admin.site.register(Model)

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
  list_display = ['id','user','name','university_name','department','batch','roll','address','student_img']

@admin.register(Gallery)
class GalleryModelAdmin(admin.ModelAdmin):
  list_display = ['id','user','gallery_img']


