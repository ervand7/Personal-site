from django.contrib.auth.models import User
from django.db import models
from django_currentuser.middleware import get_current_user


class Feedback(models.Model):
    class FeedbackCategoryChoice(models.TextChoices):
        Job = "Job"
        Contribution = "Contribution"
        Other = "Other"

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255,
                                choices=FeedbackCategoryChoice.choices,
                                default=FeedbackCategoryChoice.Job)
    content = models.TextField(blank=False, null=False)
    age_confirmation = models.BooleanField(null=False)
    image = models.ImageField(
        upload_to="feedback_images/%Y/%m/%d/", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.id} | {self.category}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.user_id = get_current_user().id
        return super().save(force_insert, force_update, using, update_fields)

    @property
    def as_dict(self):
        return {
            "description": self.description,
            "category": self.category,
            "content": self.content,
            "age_confirmation": self.age_confirmation
        }
