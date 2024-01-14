from django.db import models

# Create your models here.


class Username(models.Model):
    nick = models.CharField(max_length=30, default='redduckz')

    def __str__(self):
        return self.nick