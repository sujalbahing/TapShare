from django.db import models
import random
import string
import os
from django.utils import timezone
# from datetime import timedelta

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    code = models.CharField(max_length=8, unique=True, editable=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(random.choices(string.digits, k=4))
            # self.expiration_date = timezone.now() + timedelta(minutes=1)
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        # Delete the file from storage
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(*args, **kwargs)
        
    def is_expired(self):
        return timezone.now() > self.expiration_date
        
    
