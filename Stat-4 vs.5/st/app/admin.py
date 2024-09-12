from django.contrib import admin
from . models import Student,Gallery,BlogPost
# Register your models here.




from .models import PDFDocument,DataPoint

@admin.action(description='Approve selected PDFs')
def approve_pdfs(modeladmin, request, queryset):
    queryset.update(pending=False)

class PDFDocumentAdmin(admin.ModelAdmin):
    list_display = ('user', 'document', 'uploaded_at', 'pending')
    list_filter = ('pending', 'uploaded_at', 'user')
    actions = [approve_pdfs]

admin.site.register(PDFDocument, PDFDocumentAdmin)
@admin.register(DataPoint)
class DataPointAdmin(admin.ModelAdmin):
    list_display = ('user', 'labels', 'values')
    search_fields = ('user__username', 'labels')
admin.site.register(BlogPost)

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
  list_display = ['id','user','name','university_name','department','batch','roll','address','student_img']

@admin.register(Gallery)
class GalleryModelAdmin(admin.ModelAdmin):
  list_display = ['id','user','gallery_img']


