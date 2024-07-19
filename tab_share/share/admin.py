from django.contrib import admin
from .models import UploadedFile

@admin.register(UploadedFile)
class UploadFileModelAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at', 'expiration_date')
