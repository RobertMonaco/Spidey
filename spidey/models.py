from django.db import models
from django.core.files.storage import default_storage


class SpiderPic(models.Model):
    description = models.CharField(max_length=255, blank=True)
    pic = models.FileField(upload_to='static/uploads')
    uploaded_at = models.DateTimeField(auto_now_add=True)
