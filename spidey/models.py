from django.db import models


class SpiderPic(models.Model):
    description = models.CharField(max_length=255, blank=True)
    pic = models.FileField(upload_to='spidey/static/uploads')
    uploaded_at = models.DateTimeField(auto_now_add=True)
