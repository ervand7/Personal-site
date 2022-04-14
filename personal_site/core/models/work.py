from django.db import models


class Work(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, blank=True)
    about_experience = models.TextField(max_length=2000, blank=True)
    position = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    start = models.DateField(verbose_name='time of start working')
    end = models.DateField(verbose_name='time of end working', null=True, blank=True)
    site = models.URLField(verbose_name='work url address', null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'work'
        verbose_name_plural = 'works'
        ordering = ['-start', 'name']
