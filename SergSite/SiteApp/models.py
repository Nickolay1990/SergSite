from django.db import models


class LinkModel(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name
