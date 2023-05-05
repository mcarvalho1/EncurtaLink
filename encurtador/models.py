from django.db import models

# Create your models here.

class EncurtadorModel(models.Model):
    link = models.CharField(verbose_name='link', max_length=1000)
    uid = models.CharField(verbose_name='id', max_length=5)