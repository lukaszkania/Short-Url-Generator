from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.URLField() # Url to be shorted
    shorted_url = models.URLField() # Shorted url

    def __str__(self):
        return self.shorted_url