from django.db import models
from django.utils import timezone
import random

class GhostPost(models.Model):
    type_of_post = models.BooleanField(default=True)
    body = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    secret = models.CharField(max_length=7)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body[:7]

    @property 
    def total_votes(self):
       return self.up_votes + self.down_votes

    def secret_key(self):
        keys = 'abcdefghijklmnopqrstuv0123456789'
        self.secret = ''.join(random.sample(keys, 6))
        return self.secret
      

    

