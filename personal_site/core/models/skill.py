from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Skill(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(max_length=1000, blank=True)
    logo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    it_area = models.ForeignKey('ItArea', on_delete=models.PROTECT)
    work = models.ForeignKey('Work', on_delete=models.SET_DEFAULT,
                             default=2, related_name='skills')
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='suggested_skills')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('skill_detail', kwargs={'skill_slug': self.slug})

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'
        ordering = ['time_create', 'name']
