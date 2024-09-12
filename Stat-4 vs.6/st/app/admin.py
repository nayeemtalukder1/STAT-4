from django.contrib import admin
from . models import Student,PDFDocument

# Register your models here.
@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
  list_display = ['id','user','name','university_name','department','batch','roll','address','phone','student_img']

#post
# myapp/admin.py

from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'status')
    list_filter = ('status', 'published_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status='published')
    make_published.short_description = 'Mark selected posts as published'

#gallery

from .models import Gallery

def approve_gallery_images(modeladmin, request, queryset):
    queryset.update(status='A')
approve_gallery_images.short_description = "Approve selected gallery images"

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('user', 'gallery_img', 'status')
    list_filter = ('status', 'user')
    search_fields = ('user__username',)
    actions = [approve_gallery_images]

admin.site.register(Gallery, GalleryAdmin)
#pdf
admin.site.register(PDFDocument)

