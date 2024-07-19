# tasks.py

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.utils import timezone
from .models import UploadedFile

@shared_task
def delete_expired_files():
    now = timezone.now()
    expired_files = UploadedFile.objects.filter(expiration_date__lt=now)
    for exp_file in expired_files:
        exp_file.delete()
