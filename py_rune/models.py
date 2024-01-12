from django.db import models

# Create your models here.


class Username(models.Model):
    nick = models.CharField(max_length=30)