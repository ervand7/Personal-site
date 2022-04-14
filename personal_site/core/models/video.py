from django.db import models
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    name = models.CharField(max_length=255)
    url = EmbedVideoField()

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.name
