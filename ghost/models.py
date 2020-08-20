from django.db import models
from django.utils import timezone

class GhostPost(models.Model):
    type_of_post = models.BooleanField(default=True)
    body = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0, blank=True, editable=True)
    down_votes = models.IntegerField(default=0, blank=True, editable=True)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body[:7]

