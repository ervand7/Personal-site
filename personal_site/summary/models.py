from django.db import models


class ItArea(models.Model):
    name = models.CharField(max_length=128)
    technologies = models.ManyToManyField(
        'Technology', related_name='it_areas', through='TechnologyITArea')

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=128)
    link = models.URLField(null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class TechnologyITArea(models.Model):
    it_area = models.ForeignKey(ItArea, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.it_area} | {self.technology}'
