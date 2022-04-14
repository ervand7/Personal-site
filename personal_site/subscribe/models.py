from django.contrib.auth.models import User
from django.db import models


class Subscription(models.Model):
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True)  # fill by trigger in migration
    daily = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')

    def __str__(self):
        return str(self.id)
